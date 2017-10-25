from Login import LoginPage
from Recent import RecentPage
from CreateCowork import CreateCoworkPage
from Cowork import CoworkPage
from pageRegistry import PageRegister
from functools import partial


class App(object):
    def __init__(self, driver, platformPage):
        self.pages = PageRegister.pages()
        self.platformPage = platformPage
        self.driver = driver

    def __getattr__(self, page_name):
        try:
            page_cls = self.pages[page_name]
            page_cls.__bases__ = (self.platformPage,)
            return partial(page_cls, driver=self.driver)
        except KeyError:
            raise RuntimeError("Failed to find %s" % page_name)
