from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver.get()
# driver.current_url
# driver.back()
# driver.forward()
# driver.refresh()
# driver.title
# driver.minimize_window()
#driver.fullscreen_window()
# driver.maximize_window()
# driver.close()
# driver.quit()




class SeleniumMethods():
    def browser_methods(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.in/")
        driver.maximize_window()
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.LINK_TEXT,"Today's Deals").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.minimize_window()
        time.sleep(4)
        driver.quit()

demoseleniummethodsem=SeleniumMethods()
demoseleniummethodsem.browser_methods()