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


class AndroidResource(Resource):
    PLATFORM = Platform.ANDROID

    class conponent:
        # login page
        USERNAME = (By.ID, 'com.picowork.dev.app:id/layout_edit_account')
        PASSWORD = (By.ID, 'com.picowork.dev.app:id/edit_password')
        LOGIN = (By.ID, 'com.picowork.dev.app:id/button_login')
        LOGIN_ERROR = (By.ID, 'com.picowork.dev.app:id/text_error')
        # recent page
        RECENT_TITLE = (By.ID, 'com.picowork.dev.app:id/text_title')
        CREATE_COWORK = (By.ID, 'com.picowork.dev.app:id/button_create_work')
        # create cowork page
        WORK_TITLE = (By.ID, 'com.picowork.dev.app:id/edit_work_title')
        WORK_DESC = (By.ID, 'com.picowork.dev.app:id/edit_work_desc')
        ACCESS = (By.ID, 'com.picowork.dev.app:id/switch_work_access')
        IMAGE = (By.ID, 'com.picowork.dev.app:id/image_cover')
        CREATE_BUTTON = (By.ID, 'com.picowork.dev.app:id/button_create')
        # cowork page
        COWORK_CHARTROOM_TAB = (By.ID, 'com.picowork.dev.app:id/button_work_chatroom')
        COWORK_CHATROOM_ADD_BUTTON = (By.ID, 'com.picowork.dev.app:id/button_upload_file')
        COWORK_CHATROOM_CHOOSE_PHOTO_BUTTON = (By.ID, 'com.picowork.dev.app:id/button_pick_image')
        COWORK_CHATROOM_CHOOSE_FILE_BUTTON = (By.ID, 'com.picowork.dev.app:id/button_choose_file')
        COWORK_FILE_TAB = (By.ID, 'com.picowork.dev.app:id/button_work_matter_list')
        COWORK_FILE_ADD_BUTTON = (By.ID, 'com.picowork.dev.app:id/button_upload_files')
        COWORK_FILE_CHOOSE_PHOTO_BUTTON = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]')
        COWORK_FILE_CHOOSE_FILE_BUTTON = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]')

    class message:
        LOGIN_FAILURE = 'Could not login. Please check your email, mobile number or password again.'

class iOSResource(Resource):
    PLATFORM = Platform.IOS

    class conponent:
        # login page
        USERNAME = (By.XPATH, '//XCUIElementTypeTextField')
        PASSWORD = (By.XPATH, '//XCUIElementTypeSecureTextField')
        LOGIN = (By.NAME, 'Login')
        LOGIN_ERROR = (By.NAME, 'You entered the wrong password')
        LOGIN_ERROR_ALERT = (By.NAME, 'Please re-enter ')
        # recent page
        RECENT_TITLE = (By.NAME, 'Recent')
        CREATE_COWORK = (By.ID, 'image add')
        # create cowork page
        WORK_TITLE = (By.XPATH, '//XCUIElementTypeApplication[@name="Picowork Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[1]')
        WORK_DESC = (By.XPATH, '//XCUIElementTypeApplication[@name="Picowork Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[2]')
        ACCESS = (By.XPATH, '//XCUIElementTypeApplication[@name="Picowork Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSwitch')
        IMAGE = (By.NAME, 'image pick picture')
        CREATE_BUTTON = (By.NAME, 'Create')
        # cowork page
        COWORK_CHARTROOM_TAB = (By.NAME, 'Chatroom')
        COWORK_CHATROOM_ADD_BUTTON = (By.NAME, 'image messenger attachment')
        COWORK_CHARTROOM_CHOOSE_PHOTO_BUTTON = (By.XPATH, '//XCUIElementTypeApplication[@name="Picowork Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]/XCUIElementTypeButton')
        COWORK_FILE_TAB = (By.NAME, 'File')
        COWORK_FILE_ADD_BUTTON = (By.NAME, 'image add')
        COWORK_FILE_CHOOSE_PHOTO_BUTTON = (By.NAME, 'Choose photo')

    class message:
        LOGIN_FAILURE = 'You entered the wrong password'

class WebResource(Resource):
    PLATFORM = Platform.WEB
    class conponent:
        # login page
        USERNAME = (By.NAME, 'user[email]')
        PASSWORD = (By.NAME, 'user[password]')
        LOGIN = (By.CSS_SELECTOR, 'div[class=uk-form-row]')
        LOGIN_ERROR = (By.CSS_SELECTOR, 'div[class="alert alert-error alert-right"]')
        # recent page
        RECENT_TITLE = (By.CSS_SELECTOR, 'div[class=current-user]')
        CREATE_COWORK = (By.CSS_SELECTOR, 'i[class=icon-add_work]')
        # create cowork page
        WORK_TITLE = (By.NAME, 'work[title]')
        WORK_DESC = (By.NAME, 'work[desc]')
        ACCESS = (By.CSS_SELECTOR, 'button.uk-button ng-binding')
        IMAGE = (By.CSS_SELECTOR, 'div.drop-zone')
        CREATE_BUTTON = (By.CSS_SELECTOR, 'div input[class~=confirm]')
        # cowork page
        COWORK_CHATROOM_ADD_BUTTON = (By.CSS_SELECTOR, 'button[class=uk-button uk-button-primary attachment-btn]')
        COWORK_CHATROOM_CHOOSE_PHOTO_BUTTON = (By.CSS_SELECTOR, 'button[class=file-trigger-btn uk-button uk-button-primary]')
        COWORK_CHATROOM_CHOOSE_FILE_BUTTON = (By.CSS_SELECTOR, 'button[class=file-trigger-btn uk-button uk-button-primary]')
        COWORK_FILE_ADD_BUTTON = (By.CSS_SELECTOR, 'li[class=add-file]')
        COWORK_FILE_CHOOSE_FILE_BUTTON = (By.CSS_SELECTOR, 'div[class=file-top-panel uk-panel]')

    class message:
        LOGIN_FAILURE = 'Invalid email or password.'
