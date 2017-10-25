from Page import BasePage
from pageRegistry import PageRegister
from selenium.webdriver.common.by import By

@PageRegister.register("get_recent_page")
class RecentPage(BasePage):

    def is_ready(self):
        try:
            self.driver.find_element(*self.resource.conponent.RECENT_TITLE)
        except :
            return False
        else:
            return True

    def create_cowork(self):
        self.driver.find_element(*self.resource.conponent.CREATE_COWORK).click()

    def get_into_conversation(self, name):
        self.driver.find_element(By.NAME, name).click()
