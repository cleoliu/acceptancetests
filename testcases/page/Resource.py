import os
from selenium.webdriver.common.by import By


class Platform(object):
    BASE = 'base'
    IOS = 'ios'
    ANDROID = 'android'
    WEB = 'web'
    DESKTOP = 'desktop'


class ResourceFactory(object):
    def __init__(cls, platform):
        cls.PLATFORM = platform

    def create_resource(cls):
        if cls.PLATFORM.lower() == Platform.ANDROID:
            return AndroidResource
        elif cls.PLATFORM.lower() == Platform.IOS:
            return iOSResource
        elif cls.PLATFORM.lower() == Platform.WEB:
            return WebResource
        else:
            raise Exception('Not support platform')


class Resource(object):
    PLATFORM = Platform.BASE
    RES_ROOT = os.path.join(os.getcwd(), 'testcases/data/res/')
    PLATFORM_TEMP_ROOT = os.path.join(RES_ROOT, 'temp_files/')
    TARGET_FOLDER = os.path.join(RES_ROOT, 'test_targets/')
    FILE_FOLDER = os.path.join(TARGET_FOLDER, 'file/')
    PICTURE_FOLDER = os.path.join(TARGET_FOLDER, 'picture/')
    VIDEO_FOLDER = os.path.join(TARGET_FOLDER, 'video/')
    AUDIO_FOLDER = os.path.join(TARGET_FOLDER, 'audio/')
    EXPECTED_FOLDER = os.path.join(RES_ROOT, 'expected_results/')


class AndroidResource(Resource):
    PLATFORM = Platform.ANDROID
    CUT_SIZE = (194, 1795, 0, 1080)

    class conponent:
        # main tab
        MAIN_TAB_CONTACTS = (By.ID, 'com.picowork.dev.app:id/tab_contact_list')
        MAIN_TAB_RECENT = (By.ID, 'com.picowork.dev.app:id/tab_chatroom_list')
        MAIN_TAB_NOTIFICATIONS = (By.ID, 'com.picowork.dev.app:id/button_drawer')
        MAIN_USER_DRAWER = (By.ID, 'com.picowork.dev.app:id/tab_notification_list')

        # Contacts page
        CONTACTS_TITLE = (By.ID, 'com.picowork.dev.app:id/text_title')
        CONTACTS_MAN = (By.ID, 'com.picowork.dev.app:id/text_name')
        CONTACTS_MENU_CHAT = (By.ID, 'com.picowork.dev.app:id/button_chat')

        # Chatroom page
        CHATROOM_INPUT_MESSAGE = (By.ID, 'com.picowork.dev.app:id/edit_message')
        CHATROOM_SEND_MESSAGE = (By.ID, 'com.picowork.dev.app:id/button_send_message')
        CHATROOM_MESSAGES = (By.ID, 'com.picowork.dev.app:id/text_message')
        CHATROOM_MESSAGE_SENDING = (By.ID, 'com.picowork.dev.app:id/loading')
        CHATROOM_MESSAGE_SEND_FAIL = (By.ID, 'com.picowork.dev.app:id/image_send_message_fail')
        CHATROOM_GO_BACK = (By.ID, 'com.picowork.dev.app:id/button_back')
        CHATROOM_LINK_TITLE = (By.ID, 'com.picowork.dev.app:id/text_thumb_info')

        # login page
        USERNAME = (By.ID, 'com.picowork.dev.app:id/layout_edit_account')
        PASSWORD = (By.ID, 'com.picowork.dev.app:id/edit_password')
        LOGIN = (By.ID, 'com.picowork.dev.app:id/button_login')
        LOGIN_ERROR = (By.ID, 'com.picowork.dev.app:id/text_error')

        # recent page
        RECENT_TITLE = (By.ID, 'com.picowork.dev.app:id/text_title')
        CREATE_COWORK = (By.ID, 'com.picowork.dev.app:id/button_create_work')
        COWORK = (By.ID, 'com.picowork.dev.app:id/text_title')

        # create cowork page
        WORK_TITLE = (By.ID, 'com.picowork.dev.app:id/edit_work_title')
        WORK_DESC = (By.ID, 'com.picowork.dev.app:id/edit_work_desc')
        ACCESS = (By.ID, 'com.picowork.dev.app:id/switch_work_access')
        ACCESS_CONFIRM = (By.ID, 'android:id/button2')
        IMAGE = (By.ID, 'com.picowork.dev.app:id/image_cover')
        CREATE_BUTTON = (By.ID, 'com.picowork.dev.app:id/button_create')

        # cowork page
        COWORK_CHARTROOM_TAB = (
            By.ID, 'com.picowork.dev.app:id/button_work_chatroom')
        COWORK_CHATROOM_ADD_BUTTON = (
            By.ID, 'com.picowork.dev.app:id/button_upload_file')
        COWORK_CHATROOM_CHOOSE_PHOTO_BUTTON = (
            By.ID, 'com.picowork.dev.app:id/button_pick_image')
        COWORK_CHATROOM_CHOOSE_FILE_BUTTON = (
            By.ID, 'com.picowork.dev.app:id/button_choose_file')
        COWORK_FILE_TAB = (
            By.ID, 'com.picowork.dev.app:id/button_work_matter_list')
        COWORK_FILE_ADD_BUTTON = (
            By.ID, 'com.picowork.dev.app:id/button_upload_files')
        COWORK_FILE_CHOOSE_PHOTO_BUTTON = (
            By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]')
        COWORK_FILE_CHOOSE_FILE_BUTTON = (
            By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]')
        COWORK_CHATROOM_MESSAGE = (By.CLASS_NAME, 'android.widget.TextView')
        COWORK_PHOTOTS_TITLE = (
            By.ID, 'com.google.android.apps.photos:id/title')
        COWORK_UPLOADED_PHOTO = (By.CLASS_NAME, 'android.view.ViewGroup')
        COWORK_UPLOAD_PHOTO_COMFIRM = (
            By.ID, 'com.google.android.apps.photos:id/done_button')
        COWORK_CLICK_IMAGE = (By.ID, 'com.picowork.dev.app:id/image')
        COWORK_CLICK_BACK_FROM_IMAGE = (
            By.ID, 'com.picowork.dev.app:id/button_back')
        COWORK_FILE_CLASSIFICATION = (By.CLASS_NAME, 'android.widget.TextView')
        COWORK_FILE = (By.CLASS_NAME, 'android.widget.TextView')
        COWORK_FILE_LIST_VIEW = (By.ID, 'List view')
        COWORK_FILE_UPLOADING = (By.ID, 'com.picowork.dev.app:id/loading')

    class message:
        LOGIN_FAILURE = 'Could not login. Please check your email, mobile number or password again.'


class iOSResource(Resource):
    PLATFORM = Platform.IOS
    CUT_SIZE = (140, 1334, 0, 750)

    class conponent:
        # main tab
        MAIN_TAB_CONTACTS = (By.NAME, 'show_contact_list')
        MAIN_TAB_RECENT = (By.NAME, 'show_recent_list')

        # contacts page
        CONTACTS_TITLE = (By.NAME, 'Contacts')
        CONTACTS_MAN = (By.NAME, 'contact')

        # chatroom page
        CHATROOM_INPUT_MESSAGE = (By.NAME, 'enter_text')
        CHATROOM_MESSAGES = (By.NAME, 'text')
        CHATROOM_SEND_MESSAGE = (By.NAME, 'send')
        CHATROOM_MESSAGE_SENDING = (By.ID, 'sending')
        CHATROOM_GO_BACK = (By.NAME, 'image back')
        CHATROOM_LINK_TITLE = (By.NAME, 'title')

        # login page
        USERNAME = (By.XPATH, '//XCUIElementTypeTextField')
        PASSWORD = (By.XPATH, '//XCUIElementTypeSecureTextField')
        LOGIN = (By.NAME, 'Login')
        LOGIN_ERROR = (By.NAME, 'You entered the wrong password')
        LOGIN_ERROR_ALERT = (By.NAME, 'Please re-enter ')

        # recent page
        RECENT_TITLE = (By.NAME, 'Recent')
        CREATE_COWORK = (By.ID, 'image add')
        COWORK = (By.XPATH, '//XCUIElementTypeStaticText')

        # create cowork page
        WORK_TITLE = (
            By.XPATH, '//XCUIElementTypeApplication[@name="Picowork Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[1]')
        WORK_DESC = (By.XPATH, '//XCUIElementTypeApplication[@name="Picowork Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[2]')
        ACCESS = (By.CLASS_NAME, 'XCUIElementTypeSwitch')
        ACCESS_CONFIRM = (By.NAME, 'OK')
        IMAGE = (By.NAME, 'image pick picture')
        CREATE_BUTTON = (By.NAME, 'Create')

        # cowork page
        COWORK_CHARTROOM_TAB = (By.NAME, 'Chatroom')
        COWORK_CHATROOM_ADD_BUTTON = (By.NAME, 'media')
        COWORK_CHATROOM_CHOOSE_PHOTO_BUTTON = (By.NAME, 'Choose photo')
        COWORK_FILE_TAB = (By.NAME, 'File')
        COWORK_FILE_ADD_BUTTON = (By.ID, 'image add')
        COWORK_CLOSE = (By.NAME, 'image back')
        COWORK_CLOSE_FILE = (By.NAME, 'image close')
        COWORK_FILE_UPLOADING = (By.CLASS_NAME, 'XCUIElementTypeActivityIndicator')
        COWORK_CHATROOM_MESSAGE = (By.CLASS_NAME, 'XCUIElementTypeCell')

        # camera albums
        ALBUMS_TITLE = (By.ID, 'Camera Roll')
        ALBUMS_PICTURE = (By.CLASS_NAME, 'XCUIElementTypeCell')
        ALBUMS_CHOOSE = (By.NAME, 'Choose')


    class message:
        LOGIN_FAILURE = 'You entered the wrong password'


class WebResource(Resource):
    PLATFORM = Platform.WEB
    CUT_SIZE = (283, 1256, 513, 1787)

    class conponent:
        # login page
        USERNAME = (By.NAME, 'user[email]')
        PASSWORD = (By.NAME, 'user[password]')
        LOGIN = (By.CSS_SELECTOR, 'button[enabled]')
        LOGIN_ERROR = (By.CSS_SELECTOR,
                       'div[class="alert alert-error alert-right"]')

        # recent page
        RECENT_TITLE = (By.CSS_SELECTOR, 'div[class=current-user]')
        CREATE_COWORK = (By.CSS_SELECTOR, 'i[class=icon-add_work]')
        COWORK = (By.CSS_SELECTOR, 'h3[class="link-name ng-binding"]')

        # create cowork page
        WORK_TITLE = (By.NAME, 'work[title]')
        WORK_DESC = (By.NAME, 'work[desc]')
        ACCESS = (By.CSS_SELECTOR, 'button.uk-button ng-binding')
        IMAGE = (By.CSS_SELECTOR, 'div.drop-zone')
        CREATE_BUTTON = (By.CSS_SELECTOR, 'div input[class~=confirm]')

        # cowork page
        COWORK_CHATROOM_ADD_BUTTON = (
            By.CSS_SELECTOR, 'button[class="uk-button uk-button-primary attachment-btn"]')
        COWORK_CHATROOM_CHOOSE_FILE_BUTTON = (
            By.CSS_SELECTOR, 'session[class="ng-hide"] + input[type="file"]')
        COWORK_FILE_ADD_BUTTON = (By.CSS_SELECTOR, 'li[class=add-file]')
        COWORK_FILE_CHOOSE_FILE_BUTTON = (
            By.CSS_SELECTOR, 'div.file-top-panel.uk-panel > input[type="file"]')
        COWORK_BACK_TO_CONVERSATION = (By.ID, 'file-upload')
        COWORK_CLOSE = (By.CSS_SELECTOR, 'a.work-btn[ng-click*="win.close"]')
        COWORK_CHATROOM_MESSAGE = (
            By.CSS_SELECTOR, 'div.card-title > h6[class="ng-binding ng-scope"]')
        COWORK_CARD_TITLE = (By.CSS_SELECTOR, 'h3.u3d-dotdotdot.ng-binding.ng-scope')
        COWORK_CLOSE_FILE = (By.CSS_SELECTOR, 'li[ng-hide] > label.icon-close')
        COWORK_FILE_UPLOADING = (By.CSS_SELECTOR, 'section[class="uploader"]')
        COWORK_ADD_LINK_BUTTON = (By.CSS_SELECTOR, 'li.add-card-bar-tool > a[class="work-tool-btn"]')
        COWORK_LINK_INPUT = (By.XPATH, '//aside/*//u3d-add-card-bar/*//input[@class="u3d-input-box"]')
        COWORK_LINK_CREATE_BUTTON = (By.XPATH, '//aside/*//u3d-add-card-bar/*//button[@class="u3d-btn-01 ng-binding"]')
        DESK_GO_COWORK = (By.CSS_SELECTOR, 'div.u3d-dotdotdot.ng-binding.ng-scope')
        COWORK_ADD_APP = (By.CSS_SELECTOR, 'a.work-tool-btn > i.icon-add_webapp')

        # message
        CONTACTS_MAN = (By.CSS_SELECTOR, '*[class="friend-name ng-binding"]')
        CHATROOM_INPUT_MESSAGE = (By.CSS_SELECTOR, 'div[id="chatroomTextarea"]')
        CHATROOM_SEND_MESSAGE = (By.CSS_SELECTOR, 'button[class="uk-button uk-button-primary send-btn"]')
        CHATROOM_MESSAGES = (By.CSS_SELECTOR, 'div[class="message reply-click"] div p.ng-binding.ng-isolate-scope')
        CLOSE_COWORK= (By.CSS_SELECTOR, 'a.work-btn > i.icon-close')
        COWORRK_FRIEND = (By.CSS_SELECTOR, ' h5.user-name.ng-binding')

        # privete message
        COWORK_CONTACTS_MAN = (By.CSS_SELECTOR, 'a[class="user-info user-info-opacity"] h5.user-name.ng-binding')
        PRIVATE_CHATROOM_INPUT_MESSAGE = (By.XPATH, '(//div[@id="chatroomTextarea"])[2]')

        # add cowork firend
        OPEN_COWORK_FIERND = (By.CSS_SELECTOR, 'a[class="icon-arrow_right"]')
        ADD_ADMIN = (By.CSS_SELECTOR, 'ul.actions.ng-scope > li > i.icon-friend_add')
        SEARCH_FRIEND = (By.CSS_SELECTOR, 'input[id="searchContacts"]')
        CHEOOSE_FRIEND = (By.CSS_SELECTOR, 'h5.u3d-dotdotdot.ng-binding')
        NEXT_BUTTON = (By.CSS_SELECTOR, 'button[class="uk-button uk-button-primary ng-binding"]')
        INVITE_BUTTON = (By.CSS_SELECTOR, 'button[class="uk-button uk-button-primary ng-binding"]')

        # chat room
        CHATROOM_LINK_TITLE = COWORK_CHATROOM_MESSAGE
        CHATROOM_APP_TITLE = COWORK_CHATROOM_MESSAGE

        # web app
        WEBAPP_URL = (By.CSS_SELECTOR, 'input[name="webapp[url]"]')
        WEBAPP_NAME = (By.CSS_SELECTOR, 'input[name="webapp[title]"]')
        WEBAPP_CONFIRM = (By.CSS_SELECTOR, 'div.south > input.u3d-btn-01.confirm')

        # desktop
        APPS_BUTTON = (By.CSS_SELECTOR, 'article.service-manager.service-pad')
        APPS_LIST = (By.CSS_SELECTOR, 'article > label')
        CLOSE_APPS_LIST = (By.CSS_SELECTOR, 'a.icon-close')

    class message:
        LOGIN_FAILURE = 'Invalid email or password.'
