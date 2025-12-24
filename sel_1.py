from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Drivers/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
driver.maximize_window()

input = driver.find_element(By.NAME, 'q')
input.send_keys("Selenium 4 works!")
time.sleep(5)

button = driver.find_element(By.NAME, 'btnK')
button.click()
time.sleep(5)

#driver.quit()
