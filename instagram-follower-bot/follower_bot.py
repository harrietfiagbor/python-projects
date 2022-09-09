import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:

    def __init__(self, chrome_path):
        self.driver = webdriver.Chrome(chrome_path)  # get driver path

    def login(self, login_url, username, password):
        self.driver.get(login_url)  # get login url
        time.sleep(2)  # wait for page to load
        # fill in username
        fill_username = self.driver.find_element(By.NAME, 'username')
        fill_username.send_keys(username)
        # fill in password
        fill_password = self.driver.find_element(By.NAME, 'password')
        fill_password.send_keys(password)
        # press enter
        fill_password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self, similar_account_name):
        # find target account
        self.driver.get(f'https://www.instagram.com/{similar_account_name}')
        # click on the followers
        followers = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        # wait
        time.sleep(2)

        # scroll in pop-up window
        popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(2):
            # In this case we're executing some Javascript, that's what the execute_script() method does. The method
            # can accept the script as well as a HTML element. The modal in this case, becomes the arguments[0] in
            # the script. Then we're using Javascript to say: "scroll the top of the modal (popup) element by the
            # height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()

        self.driver.quit()
