from Page import BasePage
from pageRegistry import PageRegister
from selenium.webdriver.common.by import By

@PageRegister.register("get_create_cowork_page")
class CreateCoworkPage(BasePage):
    def set_cowork_title(self, name):
        work_title_element = self.driver_wait_until(self.resource.conponent.WORK_TITLE)
        work_title_element.clear()
        work_title_element.send_keys(name)

    def set_cowork_desc(self, description):
        work_desc_element = self.driver_wait_until(self.resource.conponent.WORK_DESC)
        work_desc_element.clear()
        work_desc_element.send_keys(description)

    def submit(self):
        self.driver_wait_until(self.resource.conponent.CREATE_BUTTON).click()

    def upload_image(self):
        pass

    def switch_access(self, is_public):
        self.driver_wait_until(self.resource.conponent.ACCESS).click()
        if is_public:
            self.driver_wait_until(self.resource.conponent.ACCESS_CONFIRM).click()
