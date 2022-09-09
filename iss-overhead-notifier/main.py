import time
import requests
import datetime as dt
import smtplib

GH_LAT = 5.564540
GH_LONG = -0.225710
USER = "codedevelopertest@gmail.com"
PASSWORD = "u&aP(+UYu$808oiZ3"
MAIN_ACCOUNT = "harrietfiagbor@gmail.com"


def iss_at_my_location():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_longitude = float(iss_response.json()["iss_position"]["longitude"])
    iss_latitude = float(iss_response.json()["iss_position"]["latitude"])
    if GH_LAT - 5 < iss_latitude < GH_LAT + 5 and GH_LONG - 5 < iss_longitude < GH_LONG + 5:
        return True
    return False


def is_dark():
    parameters = {
        "lat": GH_LAT,
        "lng": GH_LONG,
        "formatted": 0
    }

    suntimes_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    suntimes_response.raise_for_status()
    sunrise = int(suntimes_response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(suntimes_response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


while True:
    time.sleep(60)
    if iss_at_my_location() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(
                from_addr=USER,
                to_addrs=MAIN_ACCOUNT,
                msg="Subject:ISS Overhead\n\n Hey, Look up! The ISS is overhead"
            )

# TODO 1. If the ISS is close to my current position,
# TODO 2. And it is currently dark,
# TODO 3. Then send me an email to tell me to look up
