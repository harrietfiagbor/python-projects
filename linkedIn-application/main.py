import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\Development\chromedriver.exe"
PASS = os.getenv('SECRET')
PHONE = os.getenv('PHONE')
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer%20" \
               "&location=London%2C%20England%2C%20United%20Kingdom "

driver.get(LINKEDIN_URL)
# click on the sign in button
sign_in_link = driver.find_element_by_link_text("Sign in")
sign_in_link.click()

# wait for next page to load
time.sleep(5)

# login with login details
email_fill = driver.find_element_by_id("username")
email_fill.send_keys("codedevelopertest@gmail.com")
password_fill = driver.find_element_by_id("password")
password_fill.send_keys(PASS)
password_fill.send_keys(Keys.ENTER)

# jobs = driver.find_element_by_css_selector("li.jobs-search-results__list-item")
# jobs.click()

# apply to the first job
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

# fill in the phone number
fill_phone = driver.find_element_by_class_name("fb-single-line-text__input")
if fill_phone.text == "":
    fill_phone.send_keys(PHONE)

# submit the application
submit_button_1 = driver.find_element_by_css_selector("footer button")
submit_button_1.click()
# final submit
submit_button_2 = driver.find_element_by_css_selector("footer button")
submit_button_2.click()
