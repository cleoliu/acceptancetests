#! /usr/bin/python

import json
import os
import argparse
tested_devices_file = './testcases/test_metadata.json'


def generate(test_dir, platform, device_id='', target='', package_name='', package_path='', url=''):
    global tested_devices_file
    if not os.path.isfile(tested_devices_file):
        with open(tested_devices_file, 'a+') as f:
            f.write('{\"tested_devices\":[]}')

    device_data = {'test_dir': test_dir, 'platform': platform}
    if device_id:
        device_data['device_id'] = device_id
    if target:
        device_data['target'] = target
    if package_name:
        device_data['package_name'] = package_name
    if package_path:
        device_data['package_path'] = package_path
    if url:
        device_data['url'] = url

    with open(tested_devices_file, 'r+') as f:
        content = json.load(f)
        content['tested_devices'].append(device_data)
        f.seek(0)
        f.truncate()
        json.dump(content, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('platform', choices=[
                        'Android', 'iOS', 'web'], help='choice tesed platform')
    parser.add_argument('-t', '--target', choices=['dev', 'alpha'], help='tested target server')
    parser.add_argument('-n', '--package_name', default='',
                        help='package name of tested app')
    parser.add_argument('-p', '--package_path', default='',
                        help='package file path of tested app')
    parser.add_argument('-d', '--device_id', default='', help='device id')
    parser.add_argument('-u', '--url', help='web url')

    args = parser.parse_args()
    generate('./testcases/', args.platform, args.device_id, args.target,
             args.package_name, args.package_path, args.url)
