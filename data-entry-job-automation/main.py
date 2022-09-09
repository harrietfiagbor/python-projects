from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# links
FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSc_gZjkVgqllkA8tqf_fmRc24fwfIgXhCCGHNdkCpO_PIMJuQ/viewform?usp' \
            '=sf_link '
ZILLOW_SAN_FRANSCISO = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B"pagination"%3A%7B%7D%2C' \
                       '"mapBounds"%3A%7B"west"%3A-122.63039626074219%2C"east"%3A-122.23626173925781%2C"south"%3A37' \
                       '.62235296460687%2C"north"%3A37.92791421764088%7D%2C"mapZoom"%3A11%2C"isMapVisible"%3Atrue%2C' \
                       '"filterState"%3A%7B"price"%3A%7B"max"%3A872627%2C"min"%3A365956%7D%2C"beds"%3A%7B"min"%3A1%7D' \
                       '%2C"fore"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A3000%2C"min"%3A1200%7D%2C"auc"%3A%7B' \
                       '"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"fsbo"%3A' \
                       '%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C' \
                       '"isListVisible"%3Atrue%7D '

CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'

http_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9 ',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72 (Edition Campaign 34) '
}

# make a request to the zillow website.To get around captchas, it is best to used http headers
zillow_request = requests.get(ZILLOW_SAN_FRANSCISO, headers=http_header).text

# scrape the zillow website
soup = BeautifulSoup(zillow_request, 'html.parser')
# print(soup.prettify())

# make a list of all the rental links
all_links = [link.get('href') for link in soup.select(selector='.photo-cards li a')]
rental_links = []
for r_link in all_links:
    if 'http' not in r_link:
        rental_links.append(f"www.zillow.com{r_link}")
    else:
        rental_links.append(r_link)


# make a list of all the rental prices
rental_prices = [price.getText().split('/')[0] for price in soup.select(selector='.photo-cards li .list-card-price')]
# make a list of all the rental addresses
rental_addresses = [address.getText() for address in soup.select('.photo-cards li .list-card-addr')]


# ----------- automate the google form ----------------------#

# to prevent errors like executable_path has been deprecated, please pass in a
# Service object
# s = Service(ChromeDriverManager().install())
s = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=s)

for n in range(len(rental_links)):
    # open the form
    driver.get(FORM_LINK)

    # wait for form to load
    time.sleep(2)

    # fill in the address
    fill_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                 '1]/div/div[1]/input')

    # fill in the rental price
    fill_price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                               '1]/div/div[1]/input')

    # fill in the rental links
    fill_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                              '1]/div/div[1]/input')

    # find the corresponding links and prices of each address
    fill_address.send_keys(rental_addresses[n])
    fill_price.send_keys(rental_prices[n])
    fill_link.send_keys(rental_links[n])

    # submit form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

    time.sleep(2)
