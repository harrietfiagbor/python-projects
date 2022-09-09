from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# find the cookie
cookie = driver.find_element_by_id("cookie")

# set a time after 5 seconds
timeout = time.time() + 5
# set a time after 5 minutes
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    # if the time is over 5 seconds purchase upgrade items
    if time.time() > timeout:
        store_items = driver.find_elements_by_css_selector("#store div")
        for item in store_items[::-1]:
            try:
                if not item.get_attribute("class"):  # for items without a gray class
                    item.click()
            except StaleElementReferenceException:
                # when the WebElement changes. In this case, the class attribute keeps changing
                # solution is to refresh the elements or list of elements
                store_items = driver.find_elements_by_css_selector("#store div")

        # wait for another 5 seconds until next check
        timeout = time.time() + 5

    # print the cookies per second after every 5 min
    if time.time() > five_min:
        cookies_per_sec = driver.find_element_by_id("cps").text
        print(cookies_per_sec)
        break

driver.quit()
