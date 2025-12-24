from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Drivers/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://www.amazon.in/")
driver.maximize_window()

time.sleep(5)

select = driver.find_element(By.LINK_TEXT, "Mobiles")
select.click()

time.sleep(5)

#driver.quit()
