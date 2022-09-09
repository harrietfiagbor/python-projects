import os
from twilio.rest import Client
import smtplib

MY_EMAIL = os.getenv("MY_EMAIL")

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_message(self, message):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=message,
            from_='+14157543958',
            to=os.getenv("MY_PHONE_NUMBER")
        )

        print(message.status)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connnection:
            connnection.starttls()
            connnection.login(user=MY_EMAIL, password=os.getenv("MY_PASSWORD"))
            for email in emails:
                connnection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )

