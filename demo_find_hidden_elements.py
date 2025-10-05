from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class demoFinHiddenElements():
    def find_elements(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        element_state = driver.find_element(By.ID,"myDIV").is_displayed()
        print(element_state)
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        element_state1 = driver.find_element(By.ID, "myDIV").is_displayed()
        print(element_state1)

demoFindElements=demoFinHiddenElements()
demoFindElements.find_elements()