from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Drivers/chromedriver-win64/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://www.amazon.in/")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Iphones")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

list = driver.find_element(
    By.XPATH, "//h2[contains(@class,'a-size-medium')]//span"
).text

for i in list:
    print(i.text)

driver.quit()    
