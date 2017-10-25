import json
import time
from page.app import App
from contextlib import contextmanager
from collections import namedtuple


User = namedtuple('user', ['email', 'password'])

def load_default_user():
    with open('./testcases/data/users.json') as f:
        user = json.load(f)['users']
        return User(user['email'], user['password'])

def close_app(my_driver):
    try:
        my_driver.close()
    except:
        print 'Failed to close app'

@contextmanager
def app_context(my_driver, platformPage):
    time.sleep(1)
    app = App(driver=my_driver.get_driver(), platformPage=platformPage)
    my_driver.start()
    time.sleep(10)
    app.get_login_page().allow_notification()
    try:
        yield app
    finally:
        close_app(my_driver)
