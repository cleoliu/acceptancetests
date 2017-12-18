import time
from appium import webdriver as appium_driver
from selenium import webdriver as selenium_driver
from Resource import ResourceFactory, Platform
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import helper


class BasePage(object):
    def __init__(self, driver, platform):
        self.driver = driver
        self.platform = platform
        self.resource = ResourceFactory(self.platform).create_resource()

    '''
        resource must be a tuple, e.g. (By.ID, 'login')
    '''

    def driver_wait_until(self, resource, expected_conditions_func=EC.visibility_of_element_located, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions_func(resource))

    def is_element_existed(self, resource, expected_text, expected_conditions_func=EC.visibility_of_all_elements_located):
        elements = self.driver_wait_until(resource, expected_conditions_func)
        elements.reverse()
        for e in elements:
            if e.text == expected_text:
                return True
        else:
            return False

    def find_element_to_click(self, resource, expected_text, expected_conditions_func=EC.visibility_of_all_elements_located):
        elements = self.driver_wait_until(resource, expected_conditions_func)
        for e in elements:
            if e.text == expected_text:
                e.click()
                break
        else:
            assert False, 'Can not find the element by text: {}'.format(expected_text)

    def wait_element_inv(self, resource, timeout=15):
        '''
            wait element invisibility
        '''
        return self.driver_wait_until(resource, expected_conditions_func=EC.invisibility_of_element_located, timeout=timeout)

    def click_file_from_chatroom(self, file_name):
        time.sleep(2) # wait text be rendered
        self.find_element_to_click(self.resource.conponent.COWORK_CHATROOM_MESSAGE, file_name,
                                   EC.presence_of_all_elements_located)

    def allow_permission(self):
        pass

    def accept_login_error_alert(self):
        pass

    def is_conversation_exist(self, name):
        pass

    def hide_keyboard(self):
        pass

    def back_to_conversation(self):
        pass

    def _upload_photo_from_chatroom(self, file_path):
        pass

    def close_file(self):
        pass

    def get_into_conversation(self, name):
        pass

    def _upload_file_from_chatroom(self, file_path):
        pass

    def wait_file_opened(self, file_extension):
        pass

    def play_media(self):
        pass

    def show_media_title_bar(self):
        pass

    def find_contact(self):
        pass

class AndroidPage(BasePage):
    def __init__(self, driver):
        super(AndroidPage, self).__init__(driver, Platform.ANDROID)

    def is_conversation_exist(self, name):
        return self.is_element_existed((By.ID, 'com.picowork.dev.app:id/text_title'),
                                       name, EC.presence_of_all_elements_located)

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except:
            pass

    def _upload_photo_from_chatroom(self, file_name):
        self.driver_wait_until(self.resource.conponent.COWORK_CHATROOM_CHOOSE_PHOTO_BUTTON,
                               EC.presence_of_element_located).click()
        self.find_element_to_click(self.resource.conponent.COWORK_PHOTOTS_TITLE, 'Camera')

        cells = self.driver_wait_until(self.resource.conponent.COWORK_UPLOADED_PHOTO,
                                       EC.visibility_of_all_elements_located)
        index = helper.trans_picture_name_to_index(file_name)
        cells[index].click()

    def close_file(self):
        try:
            self.driver.tap([(500, 500)])
            self.driver_wait_until(
                self.resource.conponent.COWORK_CLICK_BACK_FROM_IMAGE).click()
        except :
            self.driver.press_keycode(4) # 4, press back button

    def get_into_conversation(self, name):
        self.find_element_to_click(self.resource.conponent.COWORK, name)

    def _upload_file_from_chatroom(self, file_name):
        self.driver_wait_until(
            self.resource.conponent.COWORK_CHATROOM_CHOOSE_FILE_BUTTON).click()

        try:
            self.driver_wait_until(
                self.resource.conponent.COWORK_FILE_LIST_VIEW).click()
        except Exception as e:
            print e

        def _find_and_click(file_name):
            items = self.driver_wait_until(
                self.resource.conponent.COWORK_FILE_CLASSIFICATION, EC.visibility_of_all_elements_located)

            for item in items:
                if item.text == file_name:
                    item.click()
                    self.wait_element_inv(self.resource.conponent.COWORK_FILE_UPLOADING, timeout=60)
                    return True
            else:
                return False

        if not _find_and_click(file_name):
            self.driver.swipe(350, 700, 350, 350, 500)
            assert _find_and_click(file_name), 'Failed to find the file: %s' % file_name

    def wait_file_opened(self, file_extension):
        if file_extension == 'pdf':
            self.wait_element_inv((By.CLASS_NAME, 'android.widget.ProgressBar'), timeout=30)
        else:
            # default wait
            time.sleep(2)

    def show_media_title_bar(self):
        self.driver.tap([(500, 500)])

    def find_contact(self, user_name):
        contacts = self.driver_wait_until(
            self.resource.conponent.CONTACTS_MAN, EC.visibility_of_all_elements_located)
        for contact in contacts:
            if contact.text == user_name:
                return contact
        else:
            raise RuntimeError("Contact %s not found" % user_name)

    def click_chat(self):
        self.driver_wait_until(
            self.resource.conponent.CONTACTS_MENU_CHAT).click()

    def chat_with(self, name):
        contact = self.find_contact(name)
        self.swipe_on_contact(contact)
        self.click_chat()

    def is_message_sent(self):
        self.wait_element_inv(self.resource.conponent.CHATROOM_MESSAGE_SENDING)
        self.wait_element_inv(self.resource.conponent.CHATROOM_MESSAGE_SEND_FAIL)

class iOSPage(BasePage):
    def __init__(self, driver):
        super(iOSPage, self).__init__(driver, Platform.IOS)

    def allow_permission(self):
        try:
            self.driver.switch_to.alert.accept()
        except Exception as e:
            print e

    def accept_login_error_alert(self):
        self.driver_wait_until(
            self.resource.conponent.LOGIN_ERROR_ALERT).click()

    def is_conversation_exist(self, name):
        self.driver_wait_until((By.ID, name))
        return True

    def _upload_photo_from_chatroom(self, file_path):
        self.driver.find_element(
            *self.resource.conponent.COWORK_CHATROOM_CHOOSE_PHOTO_BUTTON).click()
        self.allow_permission()
        self.driver_wait_until(self.resource.conponent.ALBUMS_TITLE).click()
        cells = self.driver_wait_until(
            self.resource.conponent.ALBUMS_PICTURE, EC.visibility_of_all_elements_located)

        index = helper.trans_picture_name_to_index(file_path)
        cells[index].click()
        if file_path.split('.')[1] in ['gif', 'mov']:
            self.driver_wait_until(
                self.resource.conponent.ALBUMS_CHOOSE).click()
        self.driver.tap([(370, 480)])
        self.wait_element_inv(self.resource.conponent.COWORK_FILE_UPLOADING)

    def close_file(self):
        self.driver_wait_until(self.resource.conponent.COWORK_CLOSE_FILE).click()

    def get_into_conversation(self, name):
        self.driver_wait_until((By.ID, name)).click()

    def click_file_from_chatroom(self, file_name):
        cells = self.driver_wait_until(
            self.resource.conponent.COWORK_CHATROOM_MESSAGE, EC.visibility_of_any_elements_located)
        cells[len(cells) - 1].click()
        time.sleep(2)

    def play_media(self):
        self.driver.tap([(500, 500)])

    def _upload_file_from_chatroom(self, file_path):
        self._upload_photo_from_chatroom(file_path)

    def find_contact(self, username):
        contacts = self.driver_wait_until((By.NAME, 'contact'), EC.presence_of_all_elements_located)
        for contact in contacts:
            e = contact.find_element(By.NAME, 'name')
            if e.text == username:
                return contact
        else:
            assert False, 'Can not find the contact: {}'.format(username)

    def click_chat(self, contact):
        contact.find_element(By.NAME, 'chat').click()

    def chat_with(self, name):
        contact = self.find_contact(name)
        self.swipe_on_contact(contact)
        self.click_chat(contact)

    def is_message_sent(self):
        self.wait_element_inv(self.resource.conponent.CHATROOM_MESSAGE_SENDING)

class WebPage(BasePage):
    def __init__(self, driver):
        super(WebPage, self).__init__(driver, Platform.WEB)

    def is_conversation_exist(self, name):
        self.driver_wait_until(
            (By.CSS_SELECTOR, 'span[title="{}"'.format(name)))
        return True

    def back_to_conversation(self):
        self.driver_wait_until(
            self.resource.conponent.COWORK_BACK_TO_CONVERSATION).click()

    def close_file(self):
        self.driver_wait_until(
            self.resource.conponent.COWORK_CLOSE_FILE).click()

    def get_into_conversation(self, name):
        self.driver_wait_until(
            (By.CSS_SELECTOR, 'span[title="{}"]'.format(name)))

    def _upload_file_from_chatroom(self, file_path):
        self.driver_wait_until(self.resource.conponent.COWORK_CHATROOM_CHOOSE_FILE_BUTTON,
                               EC.invisibility_of_element_located).send_keys(file_path)
        self.wait_element_inv(self.resource.conponent.COWORK_FILE_UPLOADING)

    def _upload_photo_from_chatroom(self, file_path):
        self._upload_file_from_chatroom(file_path)

    def wait_file_opened(self, file_extension):
        if file_extension == 'pdf':
            self.driver.switch_to_frame(self.driver_wait_until((By.XPATH, '//iframe[@class="openedIFrame"]')))
            self.driver.switch_to_frame(self.driver.find_elements(By.TAG_NAME, 'iframe')[0])
            self.driver_wait_until((By.XPATH, '//div[@id="thumbContainer0"]'), EC.visibility_of_element_located, timeout=30)
            self.driver.switch_to_default_content()
        else:
            # default wait
            time.sleep(2)

    def play_media(self):
        self.driver_wait_until((By.CSS_SELECTOR, 'span#media_view.jwmain')).click()
