from Page import BasePage
from pageRegistry import PageRegister
from selenium.webdriver.support import expected_conditions as EC


@PageRegister.register("get_login_page")
class LoginPage(BasePage):
    def set_username(self, username):
        username_element = self.driver_wait_until(self.resource.conponent.USERNAME)
        username_element.clear()
        username_element.send_keys(username)

    def set_password(self, password):
        password_element= self.driver_wait_until(self.resource.conponent.PASSWORD)
        password_element.clear()
        password_element.send_keys(password)

    def click_login(self):
        self.driver_wait_until(self.resource.conponent.LOGIN).click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    def is_failure(self):
        return self.driver_wait_until(self.resource.conponent.LOGIN_ERROR).text == self.resource.message.LOGIN_FAILURE
