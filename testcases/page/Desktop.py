from Page import BasePage
from pageRegistry import PageRegister
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@PageRegister.register("get_desktop_page")
class DesktopPage(BasePage):
    def show_apps_list(self):
        self.driver_wait_until(self.resource.conponent.APPS_BUTTON,
            EC.element_to_be_clickable).click()

    def click_app(self, app_name):
        self.find_element_to_click(self.resource.conponent.APPS_LIST, app_name)

    def is_app_exist(self, app_name):
        return self.is_element_existed(self.resource.conponent.APPS_LIST, app_name)

    def close_apps_list(self):
        self.driver_wait_until(self.resource.conponent.CLOSE_APPS_LIST,
            EC.element_to_be_clickable).click()
