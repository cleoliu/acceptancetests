import pytest
import time
import utils
import requests
import re
from page.app import App
from page.Resource import Platform


def get_web_page_title(url):
    result = requests.get(url)
    assert result.status_code == requests.codes.ok, 'Failed to get url title'
    try:
        title_pattern = r'<title[^>]*>([^<]+)</title>'
        return re.findall(title_pattern, result.content)[0]
    except Exception as e:
        print e
        assert False, 'Failed to get url title'

@pytest.fixture(scope='class')
def setup_testSendMessage_class(request, driver_setup):
    user = utils.load_default_user()
    with utils.app_context(driver_setup[0], driver_setup[1]) as app:
        app.login(user.email, user.password)
        request.cls.app = app
        yield


@pytest.mark.usefixtures('setup_testSendMessage_class')
class TestSendMessage(object):

    @pytest.fixture(scope='function')
    def create_cowork(self):
        cowork_page = self.app.get_cowork_page()
        if self.app.platform == Platform.WEB:
            cowork_page.close_cowork()
            time.sleep(3)
        else: # mobile
            cowork_page.go_back()
            self.app.get_contacts_page().click_recent()

        cowork_name = '{}_{}'.format(
            self.app.platform,
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        self.cowork_name = cowork_name
        self.app.create_cowork(cowork_name)

    @pytest.mark.skip_by_platform([Platform.WEB])
    def test_send_message_in_one_to_one_chatroom(self):
        contact_name = 'picotest_bot2'
        self.app.get_recent_page().click_contacts()
        contacts_page= self.app.get_contacts_page()
        contacts_page.chat_with(contact_name)
        message = '{}_{}'.format(self.app.platform,
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        chatroom_page = self.app.get_chatroom_page()
        chatroom_page.send_message(message)
        assert chatroom_page.is_message_exist(message), 'The message not found in chatroom'
        chatroom_page.is_message_sent()

    @pytest.mark.skip_by_platform([Platform.IOS, Platform.ANDROID])
    def test_send_message_in_one_to_one_chatroom_web(self):
        contacts_page = self.app.get_contacts_page()
        contact_name = 'picotest_bot2'
        contacts_page.click_desk_contact(contact_name)
        message = '{}_{}'.format(self.app.platform,
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        chatroom_page = self.app.get_chatroom_page()
        chatroom_page.send_message(message)
        self.app.get_cowork_page().close_cowork()
        time.sleep(3)
        self.app.get_recent_page().click_recent_list(contact_name)
        time.sleep(6)
        assert chatroom_page.is_message_exist(message), 'The message not found in chatroom'

    @pytest.mark.skip_by_platform([Platform.WEB])
    def test_send_message_in_public_chatroom(self, create_cowork):
        message = '{}_{}'.format(self.app.platform,
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        chatroom_page = self.app.get_chatroom_page()
        chatroom_page.send_message(message)
        assert chatroom_page.is_message_exist(message), 'The message not found in chatroom'
        chatroom_page.is_message_sent()

    @pytest.mark.skip_by_platform([Platform.IOS, Platform.ANDROID])
    def test_send_message_in_public_chatroom_web(self, create_cowork):
        message = '{}_{}'.format(self.app.platform,
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        chatroom_page = self.app.get_chatroom_page()
        chatroom_page.send_message(message)
        self.app.get_cowork_page().close_cowork()
        time.sleep(3)
        self.app.get_recent_page().click_recent_list(self.cowork_name)
        time.sleep(6)
        assert chatroom_page.is_message_exist(message), 'The message not found in chatroom'

    @pytest.mark.skip_by_platform([Platform.IOS, Platform.ANDROID])
    def test_send_message_in_private_chatroom_web(self, create_cowork):
        contact_name = 'picotest_bot2'
        cowork_page = self.app.get_cowork_page()
        cowork_page.add_cowork_firend(contact_name)
        contacts_page= self.app.get_contacts_page()
        contacts_page.click_cowork_contact(contact_name)
        message = '{}_{}'.format(self.app.platform,
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        chatroom_page = self.app.get_chatroom_page()
        chatroom_page.private_send_message(message)
        self.app.get_cowork_page().close_cowork()
        time.sleep(3)
        self.app.get_recent_page().click_recent_list('{} [{}]'.format(contact_name, self.cowork_name))
        time.sleep(8)
        assert chatroom_page.is_message_exist(message), 'The message not found in chatroom'

    @pytest.mark.skip_by_platform([Platform.WEB])
    def test_send_link_mobile(self, create_cowork):
        link_message = 'http://picowork.com'
        chatroom_page = self.app.get_chatroom_page()
        chatroom_page.send_message(link_message)
        assert chatroom_page.is_link_title_exist(get_web_page_title(link_message)), 'Title of link not found in chat room'

    @pytest.mark.skip_by_platform([Platform.ANDROID, Platform.IOS])
    def test_send_link_web(self, create_cowork):
        link = 'http://picowork.com'
        cowork_page = self.app.get_cowork_page()
        cowork_page.click_add_link_button()
        cowork_page.set_link(link)
        cowork_page.click_create_link_button()
        assert self.app.get_chatroom_page().is_link_title_exist(get_web_page_title(link)), 'Title of link not found in chat room'

        cowork_page.close_cowork()
        self.app.get_recent_page().click_recent_list(self.cowork_name)
        assert self.app.get_chatroom_page().is_link_title_exist(get_web_page_title(link)), 'Title of link not found in chat room'

    @pytest.mark.skip_by_platofrm([Platform.ANDROID, Platform.IOS])
    def test_send_web_app(self, create_cowork):
        link = 'http://picowork.com'
        app_name = 'app_{}'.format(self.cowork_name)
        cowork_page = self.app.get_cowork_page()
        chatroom_page = self.app.get_chatroom_page()
        desktop_page = self.app.get_desktop_page()

        # create and send webapp
        cowork_page.click_add_webapp_button()
        cowork_page.set_app_url(link)
        cowork_page.set_app_name(app_name)
        cowork_page.submit_app()
        assert chatroom_page.is_link_title_exist(app_name), 'Title of webapp not found in chat room'
        assert cowork_page.is_card_title_exist(app_name), 'Title of card not found in cospace'

        # check app showed in apps list
        cowork_page.close_cowork()
        desktop_page.show_apps_list()
        assert desktop_page.is_app_exist(app_name), 'App not found in Apps list'

        # open app to verify

        # go into cowork to check message and card are sent
        desktop_page.close_apps_list()
        self.app.get_recent_page().click_recent_list(self.cowork_name)
        assert chatroom_page.is_link_title_exist(app_name), 'Title of webapp not found in chat room'
        assert cowork_page.is_card_title_exist(app_name), 'Title of card not found in cospace'

        # open message and card of app to verify
