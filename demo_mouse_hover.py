from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Demomoudehover():
    def mouse_hover(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/flights")
        driver.maximize_window()
        ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//span[@class='more-arr']")).perform()
        sleep(3)
        driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()

        sleep(2)

mousehover = Demomoudehover()
mousehover.mouse_hover()