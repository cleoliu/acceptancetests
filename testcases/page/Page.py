from appium import webdriver as appium_driver
from selenium import webdriver as selenium_driver
from Resource import ResourceFactory, Platform
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver, platform):
        self.driver = driver
        self.platform = platform
        self.resource = ResourceFactory(self.platform).create_resource()

    def allow_notification(self):
        pass

    def accept_login_error_alert(self):
        pass

    def is_conversation_exist(self, name):
        pass

    def hide_keyboard(self):
        pass

class AndroidPage(BasePage):
    def __init__(self, driver):
        super(AndroidPage, self).__init__(driver, Platform.ANDROID)

    def is_conversation_exist(self, name):
        try:
            idents = self.driver.find_elements_by_id('com.picowork.dev.app:id/text_title')
            for ident in idents:
                if ident.get_attribute('text') == name:
                    return True
        except:
            return False
        else:
            return False

    def hide_keyboard(self):
        self.driver.hide_keyboard()

class iOSPage(BasePage):
    def __init__(self, driver):
        super(iOSPage, self).__init__(driver, Platform.IOS)

    def allow_notification(self):
        try:
            self.driver.switch_to.alert.accept()
        except Exception as e:
            print e

    def accept_login_error_alert(self):
        self.driver.find_element(
            *self.resource.conponent.LOGIN_ERROR_ALERT).click()

    def is_conversation_exist(self, name):
        try:
            self.driver.find_element(By.ID, name)
        except:
            return False
        else:
            return True

class WebPage(BasePage):
    def __init__(self, driver):
        super(WebPage, self).__init__(driver, Platform.WEB)

    def is_conversation_exist(self, name):
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'span[title="{}"'.format(name))
        except Exception as e:
            return False
        else:
            return True
