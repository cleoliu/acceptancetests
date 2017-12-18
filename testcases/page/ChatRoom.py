from Page import BasePage
from pageRegistry import PageRegister
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@PageRegister.register("get_chatroom_page")
class ChatRoomPage(BasePage):

    def send_message(self, text):
        self.driver_wait_until(
            self.resource.conponent.CHATROOM_INPUT_MESSAGE).send_keys(text)
        self.driver_wait_until(
            self.resource.conponent.CHATROOM_SEND_MESSAGE).click()

    def private_send_message(self, text):
        self.driver_wait_until(
            self.resource.conponent.PRIVATE_CHATROOM_INPUT_MESSAGE).send_keys(text)
        self.driver_wait_until(
            self.resource.conponent.CHATROOM_SEND_MESSAGE).click()

    def is_message_exist(self, text):
        return self.is_element_existed(self.resource.conponent.CHATROOM_MESSAGES,
            text, EC.presence_of_all_elements_located)

    def is_link_title_exist(self, title):
        return self.is_element_existed(self.resource.conponent.CHATROOM_LINK_TITLE,
            title)
