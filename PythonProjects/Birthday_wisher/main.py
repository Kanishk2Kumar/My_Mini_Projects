from datetime import datetime
import pandas
import random
import smtplib

today = datetime.now()
today_tuple = (today.month, today.day)

MY_EMAIL = "N12345uke@gmail.com"
Password = "qxlmdheugsgzynyz"

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    print(birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, Password)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["Email"],
                            msg=f"Subject: Happy Birthday!\n\n{contents}")
