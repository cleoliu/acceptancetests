import pytest
import time
import utils
from page.app import App


@pytest.fixture(scope='class')
def setup_login_class(request, driver_setup):
    request.cls.user =  utils.load_default_user()
    with utils.app_context(driver_setup[0], driver_setup[1]) as app:
        request.cls.app = app
        yield

@pytest.mark.usefixtures('setup_login_class')
class TestLogin(object):

    def test_login_failure(self):
        time.sleep(1)
        login_page = self.app.get_login_page()
        login_page.set_username('qary@mailinator.com')
        login_page.set_password('picowork')
        time.sleep(1)
        login_page.login()
        time.sleep(4)
        assert login_page.is_failure(), 'login seems success'
        login_page.accept_login_error_alert()

    def test_login_success(self):
        login_page = self.app.get_login_page()
        login_page.set_username(self.user.email)
        login_page.set_password(self.user.password)
        login_page.login()
        time.sleep(8)
        recent_page = self.app.get_recent_page()
        assert recent_page.is_ready(), 'Failed to go to recent page'
