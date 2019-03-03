from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///C:/Users/HP/Desktop/Webtableanuradha.html")
driver.maximize_window()
driver.implicitly_wait(30)
cell_val = driver.find_element_by_xpath("//*[@id='emp']/tbody/tr[1]/td[2]")
print(cell_val.text)
row_val = driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr")
print(row_val)
print(type(row_val))
for val in row_val:
    print(val.text)
