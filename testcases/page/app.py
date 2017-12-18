from Login import LoginPage
from Recent import RecentPage
from CreateCowork import CreateCoworkPage
from Cowork import CoworkPage
from Contacts import ContactsPage
from ChatRoom import ChatRoomPage
from Main import MainPage
from Desktop import DesktopPage
from pageRegistry import PageRegister
from functools import partial


class App(object):
    def __init__(self, driver, platformPage, platform):
        self.pages = PageRegister.pages()
        self.platformPage = platformPage
        self.driver = driver
        self.platform = platform

    def __getattr__(self, page_name):
        try:
            page_cls = self.pages[page_name]
            page_cls.__bases__ = (self.platformPage,)
            return partial(page_cls, driver=self.driver)
        except KeyError:
            raise RuntimeError('Failed to find %s' % page_name)

    def login(self, email, password):
        self.get_login_page().login(email, password)

    def create_cowork(self, name, desc='auto_desc', is_public=False):
        recent_page = self.get_recent_page()
        recent_page.create_cowork()
        create_cowork_page = self.get_create_cowork_page()
        create_cowork_page.set_cowork_title(name)
        create_cowork_page.set_cowork_desc(desc)
        if is_public:
            create_cowork_page.switch_access(is_public=is_public)
        create_cowork_page.hide_keyboard()
        create_cowork_page.submit()
        recent_page.get_into_conversation(name)
