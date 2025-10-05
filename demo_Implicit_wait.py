from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class DemoImplicitWait:
    def implicit_wait(self):
        driver = webdriver.Edge()
        driver.get("https://www.yatra.com/flights")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        dept_var = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_city']")))
        dept_var.click()
        dept_var.send_keys("New Delhi")

        dept_var.send_keys(Keys.ENTER)

        dest_var = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        dest_var.click()


        dest_var.send_keys("New York")

        dept_var.send_keys(Keys.ENTER)




        # search_result = driver.find_element(By.XPATH, "//div[@class='viewport']//div[1]/li")
        # print(len(search_result))
        # for results in search_result:
        #     print(results.text)
        #     if "New York (JFK)" in results.text:
        #         results.click()
        #         time.sleep()




ImplicitWait=DemoImplicitWait()
ImplicitWait.implicit_wait()