from Page import BasePage
from pageRegistry import PageRegister
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@PageRegister.register("get_main_page")
class MainPage(BasePage):
    def click_user_drawer(self):
        self.driver_wait_until(
            self.resource.conponent.MAIN_USER_DRAWER).click()

    def click_recent(self):
        self.driver_wait_until(
            self.resource.conponent.MAIN_TAB_RECENT).click()

    def click_contacts(self):
        self.driver_wait_until(
            self.resource.conponent.MAIN_TAB_CONTACTS).click()

    def click_notifications(self):
        self.driver_wait_until(
            self.resource.conponent.MAIN_TAB_NOTIFICATIONS).click()
