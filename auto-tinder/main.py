import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


FB_EMAIL = "harriet.fiagbor"
FB_password = "Perezina33"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")

# to avoid exceptions such as no element found, let's wait for page to load
time.sleep(7)
# find log in button and click
log_in_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div['
                                             '1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in_button.click()

# wait for page to load
time.sleep(7)
# click the login with facebook element
facebook_login = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_login.click()

# switch to the pop-up facebook login window
time.sleep(7)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# fill the facebook login page with details
email_entry = driver.find_element_by_id("email")
email_entry.send_keys(FB_EMAIL)
pass_entry = driver.find_element_by_id("pass")
pass_entry.send_keys(FB_password)
pass_entry.send_keys(Keys.ENTER)

# switch to main window
time.sleep(2)
driver.switch_to.window(base_window)
print(driver.title)




