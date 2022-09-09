import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 10
PROMISED_UP = 150


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down = 0  # initialize download speed
        self.up = 0  # initialize upload speed

    def get_internet_speed(self, speed_test_url):
        # load speed test web gae
        self.driver.get(speed_test_url)
        # allow to load for some time
        time.sleep(3)
        # click on the GO button
        go_button = self.driver.find_element(By.CSS_SELECTOR, '.start-button .start-text')
        go_button.click()
        # allow to load depending on internet speed
        time.sleep(60)
        # get download speed
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                       '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                       '2]/div/div[2]/span').text
        # get upload speed
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                     '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div['
                                                     '2]/span').text

    def tweet_at_provider(self, twitter_login_url, twitter_username, twitter_pass):
        # load the twitter login page
        self.driver.get(twitter_login_url)

        # wait for page to load
        time.sleep(15)

        # input username
        fill_username = self.driver.find_element(By.NAME, "username")
        fill_username.send_keys(twitter_username)
        # press enter
        fill_username.send_keys(Keys.ENTER)

        # wait for page to load
        time.sleep(10)

        # input password
        fill_pass = self.driver.find_element(By.NAME, "password")
        fill_pass.send_keys(twitter_pass)
        # press enter
        fill_pass.send_keys(Keys.ENTER)

        # wait for page to load
        time.sleep(5)

        # send tweet
        tweet_message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up " \
                        f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
        tweet_compose = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div['
                                                           '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                           '1]/div/div/div/div[2]/div['
                                                           '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                           '1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_compose.send_keys(tweet_message)
        tweet_send = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div['
                                                        '2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div['
                                                        '2]/div[3]')
        tweet_send.click()

        time.sleep(5)
        # close the browser
        self.driver.quit()
