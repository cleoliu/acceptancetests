from Page import BasePage
from page.Resource import Platform
from pageRegistry import PageRegister
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@PageRegister.register("get_contacts_page")
class ContactsPage(BasePage):

    def swipe_on_contact(self, contact):
        center_x, center_y = contact.location['x'] + contact.size['width'] / 2, \
            contact.location['y'] + contact.size['height'] / 2

        # workaround the ios swipe issue
        offset_x, offset_y = -100, 0
        if self.platform == Platform.IOS:
            end_x, end_y, duration = offset_x, offset_y, 100
        elif self.platform == Platform.ANDROID:
            end_x, end_y, duration = center_x + offset_x, center_y + offset_y, 500

        self.driver.swipe(center_x, center_y, end_x, end_y, duration)

    def click_recent(self):
        self.driver_wait_until(self.resource.conponent.MAIN_TAB_RECENT).click()

    def click_desk_contact(self, contact_name):
        self.find_element_to_click(self.resource.conponent.CONTACTS_MAN, contact_name)

    def click_cowork_contact(self, contact_name):
        self.find_element_to_click(self.resource.conponent.COWORK_CONTACTS_MAN, contact_name)
