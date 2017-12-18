from Page import BasePage
from pageRegistry import PageRegister
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@PageRegister.register("get_cowork_page")
class CoworkPage(BasePage):

    def tap_chatroom(self):
        self.driver_wait_until(self.resource.conponent.COWORK_CHATROOM_TAB).click()

    def tap_file(self):
        self.driver_wait_until(self.resource.conponent.COWORK_FILE_TAB).click()

    def upload_photo_from_chatroom(self, file_path):
        self.driver_wait_until(self.resource.conponent.COWORK_CHATROOM_ADD_BUTTON).click()
        self._upload_photo_from_chatroom(file_path)

    def upload_photo_from_cospace(self, file_path):
        self.driver_wait_until(self.resource.conponent.COWORK_FILE_ADD_BUTTON).click()
        self.driver_wait_until(self.resource.conponent.COWORK_FILE_CHOOSE_FILE_BUTTON,
                               EC.invisibility_of_element_located).send_keys(file_path)
        self.back_to_conversation()

    def upload_file_from_chatroom(self, file_path):
        self.driver_wait_until(self.resource.conponent.COWORK_CHATROOM_ADD_BUTTON).click()
        self._upload_file_from_chatroom(file_path)

    def upload_file_from_cospace(self, file_path):
        self.driver_wait_until(self.resource.conponent.COWORK_FILE_ADD_BUTTON).click()
        self.driver_wait_until(self.resource.conponent.COWORK_FILE_CHOOSE_FILE_BUTTON).click()

    def close_cowork(self):
        self.driver_wait_until(self.resource.conponent.CLOSE_COWORK,
                               EC.presence_of_element_located).click()

    def go_back(self):
        self.driver_wait_until(
            self.resource.conponent.CHATROOM_GO_BACK).click()

    def add_cowork_firend(self, contact_name):
        self.driver_wait_until(self.resource.conponent.OPEN_COWORK_FIERND).click()
        self.driver_wait_until(self.resource.conponent.ADD_ADMIN).click()
        self.driver_wait_until(self.resource.conponent.SEARCH_FRIEND).send_keys(contact_name)
        self.find_element_to_click(self.resource.conponent.CHEOOSE_FRIEND,
            contact_name, EC.presence_of_all_elements_located)
        self.driver_wait_until(self.resource.conponent.NEXT_BUTTON).click()
        self.driver_wait_until(self.resource.conponent.INVITE_BUTTON).click()

    def click_add_link_button(self):
        self.driver_wait_until(self.resource.conponent.COWORK_ADD_LINK_BUTTON).click()

    def set_link(self, link):
        element = self.driver_wait_until(self.resource.conponent.COWORK_LINK_INPUT)
        element.click() # for avoid create botton be not clickable
        element.send_keys(link)

    def click_create_link_button(self):
        self.driver_wait_until(self.resource.conponent.COWORK_LINK_CREATE_BUTTON).click()

    def click_add_webapp_button(self):
        self.driver_wait_until(
            self.resource.conponent.COWORK_ADD_APP, EC.element_to_be_clickable).click()

    def set_app_url(self, url):
        self.driver_wait_until(self.resource.conponent.WEBAPP_URL).send_keys(url)

    def set_app_name(self, name):
        self.driver_wait_until(self.resource.conponent.WEBAPP_NAME).send_keys(name)

    def submit_app(self):
        self.driver_wait_until(
            self.resource.conponent.WEBAPP_CONFIRM, EC.element_to_be_clickable).click()

    def is_card_title_exist(self, title):
        return self.is_element_existed(self.resource.conponent.CHATROOM_LINK_TITLE, title)

    def click_app_message(self, title):
        self.find_element_to_click(self.resource.conponent.CHATROOM_APP_TITLE, title)

    def click_app_card(self, title):
        pass
