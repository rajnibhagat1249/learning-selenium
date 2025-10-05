from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class demoFindAttribute():
    def finf_attribute(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.in/")
        driver.maximize_window()
        # class ="a-truncate-cut" aria-hidden="true" style="height: auto;" xpath="1" > Sign in for your best experience < / span >
        attribute_value = driver.find_element(By.XPATH,"//span[contains(@class,'a-truncate-cut')][normalize-space()='Sign in for your best experience']").get_attribute('aria-hidden')
        print(attribute_value)

demoFindAttribute=demoFindAttribute()
demoFindAttribute.finf_attribute()