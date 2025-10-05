from selenium import webdriver
driver=webdriver.Chrome()
#driver=webdriver.Firefox()
# driver=webdriver.Edge()

driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
driver.close()
