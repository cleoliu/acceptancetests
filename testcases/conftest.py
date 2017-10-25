import os
import pytest
import time
from helper import helper
from selenium.webdriver.chrome.options import Options
from selenium import webdriver as selenium_driver
from appium import webdriver as appium_driver
from page.Page import AndroidPage, iOSPage, WebPage
import OS
import shutil


class MyDriver(object):
    def __init__(self, platform, driver, target, capabilities):
        self.platform = platform
        self.driver = driver
        self.target_server = '%s.picowork.com' % target
        self.capabilities = capabilities

    def get_target_server(self):
        return self.target_server

    def get_driver(self):
        return self.driver

    def get_capabilities(self):
        return self.capabilities

    def restart_client(self):
        pass

    def close(self):
        pass


class MyWebDriver(MyDriver):
    def __init__(self, url, target):
        self.url = url
        chrome_options = Options()
        chrome_options.add_argument('--windows-size=1600,900')
        desired_capabilities = selenium_driver.DesiredCapabilities.CHROME
        driver = selenium_driver.Chrome(
            '/usr/local/bin/chromedriver',
            chrome_options=chrome_options,
            desired_capabilities=desired_capabilities)
        driver.implicitly_wait(30)
        super(MyWebDriver, self).__init__('web', driver, target, desired_capabilities)

        time.sleep(3)
        self.close()

    def start(self):
        self.driver.start_session(selenium_driver.DesiredCapabilities.CHROME)
        self.driver.get(self.url)
        time.sleep(10)

    def close(self):
        self.driver.close()


class MyiOSDriver(MyDriver):
    package_name_mapper = {
        'com.picowork.dev': 'com.picowork.develop'
    }

    def __init__(self, package_name, package_path, device_id, target, port=4723):
        self.package_path = os.path.abspath(package_path)
        package_name = self.package_name_mapper.get(package_name, package_name)

        desired_capabilities = {
            'platformName': 'iOS',
            'platformVersion': '11.0',
            'udid': device_id,
            'deviceName': 'iPhone 7',
            'app': self.package_path
        }

        driver = appium_driver.Remote(
            'http://localhost:%d/wd/hub' % port, desired_capabilities)
        driver.implicitly_wait(30)
        super(MyiOSDriver, self).__init__('iOS', driver, target, desired_capabilities)

    def start(self):
        self.capabilities['app'] = self.package_path
        self.driver.start_session(self.capabilities)

    def close(self):
        self.driver.quit()


class MyAndroidDriver(MyDriver):
    def __init__(self, package_name, package_path, device_id, target, port=4723, appActivity='com.picowork.ctf.app.MainActivity'):
        self.package_name = package_name
        self.package_path = package_path
        self.device_id = device_id

        device = helper.AndroidDevice(device_id)
        try:
            device.uninstall_app(package_name)
        except Exception as e:
            print 'Failed to uninstall app %s' % package_name
            print e

        device.install_app(package_path)

        desired_capabilities = {
            'platformName': 'Android',
            'deviceName': device_id,
            'appPackage': package_name,
            'appActivity': appActivity,
            'autoGrantPermissions': True
        }
        driver = appium_driver.Remote(
            'http://localhost:%d/wd/hub' % port, desired_capabilities)
        driver.implicitly_wait(30)
        super(MyAndroidDriver, self).__init__('Android', driver, target, desired_capabilities)

    def start(self):
        self.driver.start_session(self.capabilities)

    def close(self):
        self.driver.quit()


def pytest_addoption(parser):
    parser.addoption('--platform', action='store',
                     default='', help='platform: Android/iOS/web')
    parser.addoption('--device_id', action='store',
                     default='', help='device id')
    parser.addoption('--target', action='store',
                     default='', help='target tested server, validation value: dev/alpha')
    parser.addoption('--package_name', action='store',
                     default='', help='tested package name')
    parser.addoption('--package_path', action='store',
                     default='', help='tested app file path')
    parser.addoption('--url', action='store', default='', help='test web url')


def pytest_configure(config):
    if config.option.platform != 'Android':
        setattr(config.option, 'markexpr', 'not Android')


@pytest.fixture(scope='session', autouse=True)
def driver_setup(request):
    platform = request.config.option.platform.lower()
    driver = None
    platform_page = None

    if platform == 'android':
        driver = MyAndroidDriver(request.config.option.package_name,
                                 request.config.option.package_path,
                                 request.config.option.device_id,
                                 request.config.option.target)
        platform_page = AndroidPage
    elif platform == 'web':
        driver = MyWebDriver(request.config.option.url,
                             request.config.option.target)
        platform_page = WebPage
    elif platform == 'ios':
        driver = MyiOSDriver(request.config.option.package_name,
                             request.config.option.package_path,
                             request.config.option.device_id,
                             request.config.option.target)
        platform_page = iOSPage
    else:
        raise RuntimeError('Unrecognized platform: %s' % platform)

    try:
        yield driver, platform_page
    finally:
        # delete screenshot folder
        shutil.rmtree(os.getcwd()+'/res/test_cowork_'+platfrom)
