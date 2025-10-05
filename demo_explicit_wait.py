from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class demoexplicitWait():
    def explicit_wait(self):
        driver = webdriver.Edge()
        driver.get("https://login.salesforce.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "username").send_keys("user1")


explicitWait = demoexplicitWait()
explicitWait.explicit_wait()

