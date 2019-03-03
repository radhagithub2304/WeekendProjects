from selenium import webdriver
driver=webdriver.Ie(executable_path="C:/Users/HP/Desktop/Driver/IEDriverServer.exe")
driver.get("file:///C:/Users/HP/Desktop/login.html")
driver.find_element_by_id("mid").send_keys("radha")
driver.find_element_by_id("pid").send_keys("adminpassword")
driver.find_element_by_id("bid").click()
# tghjklk