import pandas
import datetime as dt
import random
import smtplib

PLACEHOLDER = "[NAME]"
USER = "codedevelopertest@gmail.com"
PASSWORD = "u&aP(+UYu$808oiZ3"

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    # print(birthday_person)
    number = random.randint(1, 3)
    filepath = f"letter_templates/letter_{number}.txt"
    with open(filepath) as letter:
        today_letter = letter.read()
        birthday_letter = today_letter.replace(PLACEHOLDER, birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(
                from_addr=USER,
                to_addrs=birthday_person.email,
                msg=f"Subject:Happy Birthday!\n\n{birthday_letter}"
            )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
