import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
service = Service(executable_path='C:/Users/Osipov/Desktop/Repos_1/Victor/chromedriver_linux64/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.maximize_window()
    driver.get('https://google.com')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
