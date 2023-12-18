from pickle import TRUE
import subprocess
import sys
subprocess.call([sys.executable, 'python.exe', 'automation_test.py', shell := TRUE])
#for remove OSError: [WinError 193] %1 is not a valid Win32 application

import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
service = ChromeService(executable_path = '/Users/Osipov/Desktop/Repos_1/Victor/chromdriver_linux64/chromedriver')
driver = webdriver.Chrome(service = service, options = options)

try:
    driver.maximize_window()
    driver.get('https://google.com')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
