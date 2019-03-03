from selenium import webdriver
driver=webdriver.Ff(executable_path="C:/Users/HP/Downloads/Browser Drivers/geckodriver-v0.24.0-win64/geckodriver.exe")
driver.get("file:///C:/Users/HP/Desktop/login.html")
driver.find_element_by_id("mid").send_keys("anuradhaadmin")
driver.find_element_by_id("pid").send_keys("password")
driver.find_element_by_id("bid").click()