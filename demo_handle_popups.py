from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Demopopups():
    def demo_popups(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()

        driver.switch_to.frame("iframeResult")

        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        sleep(2)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.accept()
        sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        driver.switch_to.alert.dismiss()
        sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        driver.switch_to.alert.send_keys("robot")
        driver.switch_to.alert.accept()
        sleep(2)

popups=Demopopups()
popups.demo_popups()