from Page import BasePage
from pageRegistry import PageRegister
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@PageRegister.register("get_recent_page")
class RecentPage(BasePage):

    def is_ready(self):
        try:
            self.driver_wait_until(self.resource.conponent.RECENT_TITLE)
        except :
            return False
        else:
            return True

    def create_cowork(self):
        self.driver_wait_until(self.resource.conponent.CREATE_COWORK).click()

    def click_contacts(self):
        self.driver_wait_until(self.resource.conponent.MAIN_TAB_CONTACTS).click()

    def click_recent_list(self, cowork_name):
        self.find_element_to_click(self.resource.conponent.DESK_GO_COWORK, cowork_name, EC.presence_of_all_elements_located)