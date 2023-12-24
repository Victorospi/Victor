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
    driver.get('https://vk.com')
    time.sleep(3)

    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys('victorospi@mail.ru')
    email_input.send_keys(Keys.ENTER)
    time.sleep(5)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys('Kasha11!')
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

    my_page = driver.find_element(By.PARTIAL_LINK_TEXT, 'My profile').click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
