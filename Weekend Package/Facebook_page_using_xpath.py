from selenium import webdriver
qspider=webdriver.Chrome()
qspider.get("https://www.facebook.com/")
qspider.maximize_window()
qspider.implicitly_wait(30)
qspider.find_element_by_id("email").send_keys("radha23041993@gmail.com")
qspider.find_element_by_id("pass").send_keys("lilyc")
qspider.find_element_by_id("u_0_b").click()