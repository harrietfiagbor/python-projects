import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5
five_min = time.time() + 60 * 5


while True:
    cookie.click()
    if time.time() > timeout:
        items = driver.find_elements_by_css_selector("#store div")
        for item in items[::-1]:
            try:
                if not item.get_attribute("class"):
                    item.click()
            except StaleElementReferenceException:
                items = driver.find_elements_by_css_selector("#store div")

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

driver.quit()