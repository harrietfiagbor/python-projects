import time
from internet_speed_twitter_bot import InternetSpeedTwitterBot

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_EMAIL = "codedevelopertest@gmail.com"
TWITTER_PHONE = "+233278886747"
TWITTER_PASS = "Perezina33"
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://m.twitter.com/login"

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

# get speed test results
bot.get_internet_speed(SPEED_TEST_URL)

# wait to load up next web page
time.sleep(10)

# tweet speed test at twitter
bot.tweet_at_provider(twitter_login_url=TWITTER_URL, twitter_username=TWITTER_PHONE, twitter_pass=TWITTER_PASS)

