import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from arg_parser import InputArgParser
from datetime import datetime

chrome_driver_path = "chromedriver.exe"  # put the path to your chromedriver here
ser = Service(chrome_driver_path)
chrome_options = Options()
port_from_settings_browser = '25325'
address = "127.0.0.1" 
os_type = 'Windows'
browser_type = 'chrome'
proxies_list = []
with open("proxies_list.txt", "r") as file:
    for line in file:
        proxies_list.append(line.strip())
checker = 0


class DriverContext:
    def __init__(self) -> None:
        global checker
        self.arg_parser = InputArgParser()
        print(
            self.arg_parser.get_instance(),
            self.arg_parser.with_proxy()
        )

        profile_name = datetime.now().strftime("%d%m%Y %H%M%S")
        profile_info = {'name': profile_name, 'os': os_type, 'browser': browser_type, 'notes': 'test'}
        if self.arg_parser.with_proxy():
            print("using proxy")
            profile_info['proxy'] = proxies_list[checker]
            checker = checker + 1
            if checker == len(proxies_list):
                checker = 0
        profile_info = json.dumps(profile_info)
        print('Creating profile')
        request = requests.post(f'http://{address}:{port_from_settings_browser}/profile/create', data=profile_info, timeout=3).json()['data']
        print(request)
        self.profile_id = request["profile_id"]
        print('Opening profile')
        request = requests.get(f'http://{address}:{port_from_settings_browser}/profile/start/{self.profile_id}', timeout=5).json()['data']
        debug_port = request['debug_port']
        chrome_options.debugger_address = f'{address}:{debug_port}'

        self.driver: webdriver = webdriver.Chrome(service=ser, options=chrome_options)
        self.driver.maximize_window()

    def __enter__(self) -> webdriver:
        print("creating a selenium agent")
        return self.driver

    def __exit__(self, exc_type, exc_val, _) -> bool:
        self.driver.quit()
        print('Closing profile')
        request = requests.get(f'http://{address}:{port_from_settings_browser}/profile/stop/{self.profile_id}', timeout=5).json()['data']
        return True
