import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.makemytrip.com")
driver.maximize_window()
driver.implictly_wait(30)
driver.find_element_by_id("header_tab_hotels").click()
driver.find_element_by_id("header_tab_holidays")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()

