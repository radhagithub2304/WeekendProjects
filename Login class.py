from selenium import webdriver
qspider=webdriver.Chrome()
qspider.get("file:///C:/Users/HP/Desktop/login.html")
qspider.maximize_window()
qspider.implicitly_wait(30)
qspider.find_element_by_id("mid").send_keys("adminlogin")
qspider.find_element_by_id("pid").send_keys("passwordanuradha")
qspider.find_element_by_id("bid").click()