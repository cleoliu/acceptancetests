import os
import pytest
import time
import json
import utils
from page.app import App
from page.Resource import Resource, Platform
from PicOpenCV import PicOpenCV as cv
from helper import helper

p_join = os.path.join


@pytest.fixture(scope='class')
def setup_TestUploadFile_class(request, driver_setup):
    my_driver = driver_setup[0]
    user = utils.load_default_user()
    screenshot_folder_path = p_join(
        Resource.PLATFORM_TEMP_ROOT, my_driver.platform, 'TestCowork')
    expected_folder_path = p_join(Resource.EXPECTED_FOLDER, my_driver.platform)
    os.mkdir(screenshot_folder_path)
    request.cls.screenshot_folder_path = screenshot_folder_path
    request.cls.expected_folder_path = expected_folder_path

    if my_driver.platform == Platform.ANDROID:
        device = helper.AndroidDevice(my_driver.device_id)
        device.push_file(Resource.FILE_FOLDER + '*', device.DOWNLOAD_PATH)
        device.push_file(Resource.VIDEO_FOLDER + 'mov.mov', device.DOWNLOAD_PATH)
        device.push_file(Resource.AUDIO_FOLDER + 'mp3.mp3', device.DOWNLOAD_PATH)
    elif my_driver.platform == Platform.IOS:
        device = helper.IOSDevice(my_driver.device_id)
        device.push_file(Resource.PICTURE_FOLDER + 'bmp.bmp')
        device.push_file(Resource.PICTURE_FOLDER + 'gif.gif')
        device.push_file(Resource.PICTURE_FOLDER + 'png.png')
        device.push_file(Resource.PICTURE_FOLDER + 'jpg.jpg')
        device.push_file(Resource.VIDEO_FOLDER + 'mov.mov')

    with utils.app_context(my_driver, driver_setup[1]) as app:
        cowork_name = '{}_{}'.format(app.platform,
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        app.login(user.email, user.password)
        app.create_cowork(cowork_name)
        request.cls.app = app
        yield

    if my_driver.platform == Platform.ANDROID:
        device.remove_file(device.DOWNLOAD_PATH + '*')
    elif my_driver.platform == Platform.IOS:
        device.remove_file(device.IOSDEVICE_PATH)

@pytest.mark.usefixtures('setup_TestUploadFile_class')
class TestUploadFile(object):
    @pytest.mark.parametrize('uploaded_picture', ['png.png', 'jpg.jpg', 'bmp.bmp', 'gif.gif'])
    def test_upload_picture_by_choose_photo_from_chatroom(self, uploaded_picture):
        file_text = uploaded_picture.split('.')[0]
        file_path  = p_join(Resource.PICTURE_FOLDER, uploaded_picture) \
            if self.app.platform == Platform.WEB else uploaded_picture
        cowork_page = self.app.get_cowork_page()
        expect_picture = p_join(self.expected_folder_path, 'cowork_%s.jpg' % file_text)
        screen_file_name = p_join(self.screenshot_folder_path, 'screen_%s.png' % file_text)
        cut_screen_file_name = p_join(self.screenshot_folder_path, 'cut_screen_%s.jpg' % file_text)

        cowork_page.upload_photo_from_chatroom(file_path)

        cowork_page.click_file_from_chatroom(uploaded_picture)
        time.sleep(2)

        self.app.driver.get_screenshot_as_file(screen_file_name)
        cv.cut_image(screen_file_name, cut_screen_file_name, cowork_page.resource.CUT_SIZE)
        cowork_page.close_file()
        assert cv.verify_file_image(cut_screen_file_name, expect_picture), 'Failed to verify uploaded image'

    @pytest.mark.skip_by_platform([Platform.IOS])
    @pytest.mark.parametrize('file_name', ['zip.zip', 'no_extension'])
    def test_upload_zip_and_no_extension_from_chatroom(self, file_name):
        file_text = file_name.split('.')[0]
        file_path  = p_join(Resource.FILE_FOLDER, file_name) \
            if self.app.platform == Platform.WEB else file_name
        cowork_page = self.app.get_cowork_page()
        expect_picture = p_join(self.expected_folder_path, 'cowork_%s.jpg' % file_text)
        screen_file_name = p_join(self.screenshot_folder_path, 'screen_%s.png' % file_text)
        cut_screen_file_name = p_join(self.screenshot_folder_path, 'cut_screen_%s.jpg' % file_text)

        cowork_page.upload_file_from_chatroom(file_path)

        cowork_page.click_file_from_chatroom(file_name)
        time.sleep(2)

        self.app.driver.get_screenshot_as_file(screen_file_name)
        cv.cut_image(screen_file_name, cut_screen_file_name, cowork_page.resource.CUT_SIZE)
        cowork_page.close_file()
        assert cv.verify_file_image(cut_screen_file_name, expect_picture)

    @pytest.mark.skip_by_platform([Platform.IOS])
    @pytest.mark.parametrize('uploaded_file', ['txt.txt', 'pdf.pdf'])
    def test_upload_txt_and_pdf_from_chatroom(self, uploaded_file):
        file_extension = uploaded_file.split('.')[1]
        cowork_page = self.app.get_cowork_page()
        expect_picture = p_join(
            self.expected_folder_path, 'cowork_%s.jpg' % file_extension)
        screen_file_name = p_join(
            self.screenshot_folder_path, 'screen_%s.png' % file_extension)
        cut_screen_file_name = p_join(
            self.screenshot_folder_path, 'cut_screen_%s.jpg' % file_extension)
        file_path = p_join(Resource.FILE_FOLDER, uploaded_file) \
            if self.app.platform == Platform.WEB else uploaded_file

        cowork_page.upload_file_from_chatroom(file_path)
        cowork_page.click_file_from_chatroom(uploaded_file)
        cowork_page.wait_file_opened(file_extension)

        self.app.driver.get_screenshot_as_file(screen_file_name)
        cv.cut_image(screen_file_name, cut_screen_file_name,
                     cowork_page.resource.CUT_SIZE)
        cowork_page.close_file()
        assert cv.verify_file_image(
            cut_screen_file_name, expect_picture), 'Failed to verify uploaded image'

    @pytest.mark.parametrize('file_name', ['mov.mov'])
    def test_upload_video_from_chatroom(self, file_name):
        cowork_page = self.app.get_cowork_page()
        file_text = file_name.split('.')[0]
        file_path  = p_join(Resource.VIDEO_FOLDER, file_name) \
            if self.app.platform == Platform.WEB else file_name
        expect_picture = p_join(self.expected_folder_path, 'cowork_%s.jpg' % file_text)
        screen_file_name = p_join(self.screenshot_folder_path, 'screen_%s.png' % file_text)
        cut_screen_file_name = p_join(self.screenshot_folder_path, 'cut_screen_%s.jpg' % file_text)

        cowork_page.upload_file_from_chatroom(file_path)
        time.sleep(4)

        cowork_page.click_file_from_chatroom(file_name)
        time.sleep(2)

        cowork_page.play_media()
        time.sleep(7)

        cowork_page.show_media_title_bar()
        self.app.driver.get_screenshot_as_file(screen_file_name)
        cv.cut_image(screen_file_name, cut_screen_file_name, cowork_page.resource.CUT_SIZE)
        cowork_page.close_file()
        assert cv.verify_file_image(cut_screen_file_name, expect_picture)

    @pytest.mark.skip_by_platform([Platform.IOS])
    @pytest.mark.parametrize('file_name', ['mp3.mp3'])
    def test_upload_audio_from_chatroom(self, file_name):
        cowork_page = self.app.get_cowork_page()
        file_text = file_name.split('.')[0]
        file_path  = p_join(Resource.AUDIO_FOLDER, file_name) \
            if self.app.platform == Platform.WEB else file_name
        expect_picture = p_join(self.expected_folder_path, 'cowork_%s.jpg' % file_text)
        screen_file_name = p_join(self.screenshot_folder_path, 'screen_%s.png' % file_text)
        cut_screen_file_name = p_join(self.screenshot_folder_path, 'cut_screen_%s.jpg' % file_text)

        cowork_page.upload_file_from_chatroom(file_path)
        time.sleep(3)

        cowork_page.click_file_from_chatroom(file_name)
        time.sleep(2)

        cowork_page.play_media()
        time.sleep(4)

        cowork_page.show_media_title_bar()
        self.app.driver.get_screenshot_as_file(screen_file_name)
        cv.cut_image(screen_file_name, cut_screen_file_name, cowork_page.resource.CUT_SIZE)
        cowork_page.close_file()
        assert cv.verify_file_image(cut_screen_file_name, expect_picture)
