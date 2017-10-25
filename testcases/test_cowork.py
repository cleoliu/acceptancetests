import pytest
import time
import json
import utils
from page.app import App


@pytest.fixture(scope='class')
def setup_cowork_class(request, driver_setup):
    request.cls.user =  utils.load_default_user()
    with utils.app_context(driver_setup[0], driver_setup[1]) as app:
        request.cls.app = app
        yield
@pytest.mark.skip
@pytest.mark.usefixtures('setup_cowork_class')
class TestCowork(object):
    COWORK_NAME = 'autotest_{}_'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    def test_add_cowork(self):
        login_page = self.app.get_login_page()
        self.COWORK_NAME += login_page.platform
        time.sleep(3)
        login_page.set_username(self.user.email)
        login_page.set_password(self.user.password)
        login_page.login()
        time.sleep(8)
        recent_page = self.app.get_recent_page()
        assert recent_page.is_ready(), 'Failed to go to recent page'

        description = 'auto_desc'
        recent_page.create_cowork()
        create_cowork_page = self.app.get_create_cowork_page()
        time.sleep(1)
        create_cowork_page.set_cowork_title(self.COWORK_NAME)
        create_cowork_page.set_cowork_desc(description)
        create_cowork_page.hide_keyboard()
        create_cowork_page.submit()
        time.sleep(3)
        assert recent_page.is_conversation_exist(self.COWORK_NAME), "{} cowork not found".format(self.COWORK_NAME)
