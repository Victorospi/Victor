import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:/Users/Osipov/Desktop/Repos_1/Victor/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()
    driver.get('https://google.com')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
