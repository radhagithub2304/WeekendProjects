from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(30)
ele=driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(ele)

#ele is webelement
driver.find_element_by_id("datepicker").click()
select_ele=driver.find_element_by_xpath()
