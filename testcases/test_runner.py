#! /usr/local/bin/python

import json
from multiprocessing import Pool
import sys
import xml.etree.ElementTree as ET
import pytest


def modify_test_result(test_result_path, platform, device_id):
    tree = ET.parse(test_result_path)
    test_suite = tree.getroot()
    for testcase in test_suite.findall('testcase'):
        classname = testcase.attrib['classname']
        testcase.attrib['classname'] = testcase.attrib['classname'].replace(
            'testcase', 'testcase.%s_%s' % (platform, device_id)).replace('acceptancetests.', '')

    tree.write(test_result_path)


# platform: Android, iOS, web, desktop, mobileweb
# package_name: com.xxx for mobile device, http://dev.picoowkr.com for web & mobileweb, applicaiton name for desktop
# package_path: api/apk for mobile device, '' for web & mobileweb, application_installer for desktop


def run_test(test_dir, platform, target, device_id='', package_name='', package_path='', url=''):
    pytest_cli_args = [
        test_dir,
        '-s',
        '-v',
        '--platform',
        platform,
        '--target',
        target,
        '--device_id',
        device_id
    ]

    if package_name:
        pytest_cli_args.extend(['--package_name', package_name])
        pytest_cli_args.extend(['--package_path', package_path])
    if url:
        pytest_cli_args.extend(['--url', url])

    test_report_name = '_'.join(['test', platform, device_id, 'result.xml'])
    pytest_cli_args.append('--junitxml=%s' % test_report_name)
    print 'run pytest with these arguments: {}'.format(' '.join(pytest_cli_args))
    ret = pytest.main(pytest_cli_args)
    modify_test_result(test_report_name, platform, device_id)
    return ret

def remove_not_run_test_params(record):
    not_run_test_params = ['enabled']
    for key in (key for key in not_run_test_params if key in record):
        del record[key]
    return record

if __name__ == '__main__':
    try:
        with open('./testcases/test_metadata.json', 'r') as f:
            test_metadata = json.load(f)
    except Exception as e:
        print e
        print 'No test metadata file be generated'
        sys.exit(1)

    results = []
    pool = Pool(processes=3)

    enabled_devices = \
        (tested_device for tested_device in test_metadata['tested_devices'] \
            if tested_device.get('enabled', True))

    devices = (remove_not_run_test_params(tested_device) for tested_device in enabled_devices)

    for tested_device in devices:
        results.append(pool.apply_async(run_test, kwds=tested_device))
    pool.close()
    pool.join()

    if any([result.get() for result in results]):
        sys.exit(1)
