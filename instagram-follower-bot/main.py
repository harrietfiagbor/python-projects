from follower_bot import InstaFollower

chrome_driver_path = 'C:\Development\chromedriver.exe'
INSTAGRAM_URL = ' https://www.instagram.com/accounts/login/'
SIMILAR_ACCOUNT = 'python.learning'
USERNAME = '_learnPython3'
PASSWORD = 'Perezina33'

bot = InstaFollower(chrome_path=chrome_driver_path)

bot.login(
    login_url=INSTAGRAM_URL,
    username=USERNAME,
    password=PASSWORD
)
bot.find_followers(similar_account_name=SIMILAR_ACCOUNT)
bot.follow()

