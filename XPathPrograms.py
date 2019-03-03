from selenium import webdriver
driver=webdriver.Firefox(executable_path="C:/Users/HP/Downloads/Browser Drivers/geckodriver-v0.24.0-win64/geckodriver.exe")
driver.get("https://www.facebook.com/")
# driver.find_element_by_id("mid").send_keys("radha")
# driver.find_element_by_id("pid").send_keys("adminpassword")
# driver.find_element_by_id("bid").click()
driver.find_element_by_xpath("//*[@id='email']").send_keys("anu")
driver.find_element_by_xpath("//*[@id='u_0_l']").send_keys("kumarii")