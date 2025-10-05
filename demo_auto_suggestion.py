from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class DemoAutoSuggestion():
    def auto_suggestion(self):
        driver = webdriver.Edge()
        driver.get("https://www.yatra.com/flights")
        driver.maximize_window()
        dept_Var = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        dept_Var.click()
        time.sleep(3)

        dept_Var.send_keys("New Delhi")
        time.sleep(2)
        dept_Var.send_keys(Keys.ENTER)
        time.sleep(4)

        dest_Var = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        dest_Var.click()
        time.sleep(3)

        dest_Var.send_keys("New York")
        time.sleep(3)
        dept_Var.send_keys(Keys.ENTER)
        time.sleep(4)



        # search_result = driver.find_element(By.XPATH, "//div[@class='viewport']//div[1]/li")
        # print(len(search_result))
        # for results in search_result:
        #     print(results.text)
        #     if "New York (JFK)" in results.text:
        #         results.click()
        #         time.sleep()




autoSuggestion=DemoAutoSuggestion()
autoSuggestion.auto_suggestion()