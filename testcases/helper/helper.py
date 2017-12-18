import os
import subprocess

data = {'bmp.bmp': 0, 'gif.gif': 1, 'png.png': 2, 'jpg.jpg': 3, 'mov.mov': 4}

def trans_picture_name_to_index(name):
    return data[name]

class HelperCmdError(Exception):
    def __init__(self, ret, message):
        self.ret, self.message = ret, message

    def __str__(self):
        return '{}({})'.format(self.message, self.ret)

def execute_cmd(cmd):
    if not cmd:
        raise ValueError("Command is empty")

    print "\nexecute cmd: {}".format(cmd)
    try:
        subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print e.returncode, e.output
        raise HelperCmdError(e.returncode, e.output)

class AndroidDevice(object):
    '''
        AndroidDevice for modeling a device
    '''
    DOWNLOAD_PATH = '/sdcard/Download/'

    def __init__(self, device_id):
        self.device_id = device_id
        self.execute_cmd = execute_cmd

    def execute_cmd_with_device_id(self, cmd):
        full_cmd = 'adb -s %s %s' % (self.device_id, cmd)
        self.execute_cmd(full_cmd)

    def install_app(self, app_path):
        '''
            install app to specified device
        '''
        # sample cmd: adb instll /path/to/apk
        cmd = "install -r %s" % app_path
        self.execute_cmd_with_device_id(cmd)

    def uninstall_app(self, package_name):
        '''
            uninstall app from specified device
        '''
        # sample cmd: adb uninstall com.picowork.dev.app
        cmd = "uninstall %s" % package_name
        self.execute_cmd_with_device_id(cmd)

    def push_file(self, target, destination):
        cmd = 'push %s %s' % (target, destination)
        self.execute_cmd_with_device_id(cmd)

    def remove_file(self, target):
        cmd = 'shell rm %s' % target
        self.execute_cmd_with_device_id(cmd)


class IOSDevice(object):
    IOSDEVICE_PATH = '/Library/Developer/CoreSimulator/Devices/'

    def __init__(self, device_id):
        self.device_id = device_id
        self.execute_cmd = execute_cmd

    def install_app(self, app_path):
        cmd = "xcrun simctl install %s %s" % (self.device_id, app_path)
        self.execute_cmd(cmd)

    def uninstall_app(self, pacakage_name):
        cmd = "xcrun simctl uninstall %s %s" % (self.device_id, pacakage_name)
        self.execute_cmd(cmd)

    def push_file(self, target):
        cmd = 'xcrun simctl addmedia booted %s' % target
        self.execute_cmd(cmd)

    def remove_file(self, destination):
        cmd = 'rm -rf ~{0}{1}/data/Media/DCIM/ ~{0}{1}/data/Media/PhotoData/'.format(destination, self.device_id)
        self.execute_cmd(cmd)
