from Page import BasePage
from pageRegistry import PageRegister
from selenium.webdriver.common.by import By


@PageRegister.register("get_login_page")
class LoginPage(BasePage):
    def set_username(self, username):
        username_element = self.driver.find_element(
            *self.resource.conponent.USERNAME)
        username_element.clear()
        username_element.send_keys(username)

    def set_password(self, password):
        password_element = self.driver.find_element(
            *self.resource.conponent.PASSWORD)
        password_element.clear()
        password_element.send_keys(password)

    def login(self):
        self.driver.find_element(*self.resource.conponent.LOGIN).click()

    def is_failure(self):
        return self.driver.find_element(
            *self.resource.conponent.LOGIN_ERROR).text == self.resource.message.LOGIN_FAILURE
