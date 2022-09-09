import requests
from bs4 import BeautifulSoup
import smtplib
# import lxml


SENDER_EMAIL = "codedevelopertest@gmail.com"
SENDER_PASS = "u&aP(+UYu$808oiZ3"
RECEIVER_EMAIL = "harrietfiagbor@gmail.com"


AMAZON_URL = "https://www.amazon.com/SAMSUNG-Included-Long-Lasting-Powerful-Performance/dp/B0996S7F94/ref=sr_1_1_sspa?dchild=1&keywords=ipad&qid=1632607036&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWTE0RDZWTU4yUjJCJmVuY3J5cHRlZElkPUEwODE4Nzg3WldOM1pNUDBDWVlQJmVuY3J5cHRlZEFkSWQ9QTA0NTkzNjZHWFVHNDQ4Sk9HU0smd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
auth_header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52 "
}

amazon_response = requests.get(AMAZON_URL, headers=auth_header).text

soup = BeautifulSoup(amazon_response, "lxml")
# print(soup.prettify())
price = float(soup.find(id="priceblock_ourprice").getText().split("$")[1])
# print(price)

buy_price = 600
if price < buy_price:
    message = "SAMSUNG Galaxy Tab S7 FE, 2021 Android Tablet 12.4 Screen WiFi 64GB S Pen Included Long-Lasting " \
              f"Battery Powerful Performance, Mystic Green is now ${price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASS)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject:Amazon Price Alert\n\n{message}\n{AMAZON_URL}"
        )