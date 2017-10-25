import subprocess


class HelperCmdError(Exception):
    def __init__(self, ret, message):
        self.ret, self.message = ret, message

    def __str__(self):
        return '{}({})'.format(self.message, self.ret)

def execute_cmd(cmd):
    if not cmd:
        raise ValueError("Command is empty")

    full_cmd = cmd.split()
    print "execute cmd: {}".format(full_cmd)
    try:
        subprocess.check_output(full_cmd)
    except subprocess.CalledProcessError as e:
        print e.returncode, e.output
        raise HelperCmdError(e.returncode, e.output)


class AndroidDevice(object):
    '''
        AndroidDevice for modeling a device
    '''

    def __init__(self, device_id):
        self.device_id = device_id
        self.execute_cmd = execute_cmd

    def execute_cmd_with_device_id(self, cmd):
        full_cmd = "adb -s %s %s" % (self.device_id, cmd)
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


class iSODevice(object):
    def __init__(self, device_id):
        self.device_id = device_id
        self.execute_cmd = execute_cmd

    def install_app(self, app_path):
        cmd = "xcrun simctl install %s %s" % (self.device_id, app_path)
        self.execute_cmd(cmd)

    def uninstall_app(self, pacakage_name):
        cmd = "xcrun simctl uninstall %s %s" % (self.device_id, pacakage_name)
        self.execute_cmd(cmd)
