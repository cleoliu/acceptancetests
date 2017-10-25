from Page import BasePage
from pageRegistry import PageRegister
from selenium.webdriver.common.by import By

@PageRegister.register("get_cowork_page")
class CoworkPage(BasePage):

    def is_ready(self, title):
        try:
            self.driver.find_element(By.NAME, title)
        except:
            return False
        else:
            return True

    def tap_chatroom(self):
        self.driver.find_element(*self.resource.conponent.COWORK_CHARTROOM_TAB).click()

    def tap_file(self):
        self.driver.find_element(*self.resource.conponent.COWORK_FILE_TAB).click()

    def upload_photo_from_chatroom(self):
        self.driver.find_element(*self.resource.conponent.COWORK_CHATROOM_ADD_BUTTON).click()
        self.driver.find_element(*self.resource.conponent.COWORK_CHATROOM_CHOOSE_PHOTO_BUTTON).click()

    def upload_photo_from_cospace(self):
        self.driver.find_element(*self.resource.conponent.COWORK_FILE_ADD_BUTTON).click()
        self.driver.find_element(*self.resource.conponent.COWORK_FILE_CHOOSE_PHOTO_BUTTON).click()

    def upload_file_from_chatroom(self):
        self.driver.find_element(*self.resource.conponent.COWORK_CHATROOM_ADD_BUTTON).click()
        self.driver.find_element(*self.resource.conponent.COWORK_CHATROOM_CHOOSE_FILE_BUTTON).click()

    def upload_file_from_cospace(self):
        self.driver.find_element(*self.resource.conponent.COWORK_FILE_ADD_BUTTON).click()
        self.driver.find_element(*self.resource.conponent.COWORK_FILE_CHOOSE_FILE_BUTTON).click()

    def allow_notification(self):
        self.driver.tap([250, 380])
