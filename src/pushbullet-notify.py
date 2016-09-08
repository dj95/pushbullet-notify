#!/usr/bin/env python3
#
# pushbullet-notify
#
# (c) 2016 Daniel Jankowski


import os
import json
import argparse
import urllib.parse
import urllib.request


CONFIG_PATH = '~/.pushbullet-notify.conf'


def send_push(title, message, access_token, iden):
    # Do this for every device to inform mutliple devices
    for device in iden:
        # Build post data
        post_data = {
                'device_iden': device,
                'type': 'note',
                'title': title,
                'body': message
                }

        # Build request
        request = urllib.request.Request('https://api.pushbullet.com/v2/pushes',
                urllib.parse.urlencode(post_data).encode('utf-8'))
        request.add_header("Access-Token", access_token)
        
        # Send request
        data = urllib.request.urlopen(request).read()


def send_request(url, access_token):
    # Build request
    request = urllib.request.Request('https://api.pushbullet.com/v2/' + url)
    request.add_header("Access-Token", access_token)

    # Send request and get data
    data = urllib.request.urlopen(request).read()
    data = json.loads(data.decode('utf-8'))

    # List only specific data from the api
    for device in data['devices']:
        print('{nickname}({type}) - {iden}'.format(nickname=device['nickname'],
            type=device['type'], iden=device['iden']))


def main():
    # Argument Parser
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', action='store_true', help='Get device identifier')
    parser.add_argument('-t', type=str, help='Title of the message')
    parser.add_argument('-m', type=str, help='Body of the message')
    parser.add_argument('-c', '--config', type=str, help='Define config file')

    args = parser.parse_args()

    
    if args.config:
        config_path = args.config
    else:
        config_path = CONFIG_PATH

    # Read config file
    config_path = os.path.expanduser(os.path.normpath(config_path))
    print(config_path)
    if not os.path.isfile(config_path):
        print('Error! Cannot read the config file')
        return 0

    # Read config file
    with open(config_path, 'r') as fp:
        config = json.load(fp)

    if args.d: # List all devices to get the identifier
        send_request('devices', config['application_token'])
        return
    else: # Send push to device
        if args.t is None:
            print('Error! Missing title')
            return 0
        if args.m is None:
            message = ''
        else:
            message = args.m
        send_push(args.t, message, config['application_token'],
                config['device_iden'])
        return


if __name__ == '__main__':
    main()
