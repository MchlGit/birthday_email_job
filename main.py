import datetime as dt
import pandas as pd
import smtplib
from random import randint
import os

my_email = os.environ.get("MY_EMAIL")
my_pswd = os.environ.get("MY_PSWD")

data = pd.read_csv("birthdays.csv")
b_dict = {dt.date(year=row["year"], month=row["month"], day=row["day"]):{"name":row["name"], "email":row["email"] } for (_, row) in data.iterrows()}

now = dt.datetime.now()

def get_message(name):
    path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(path, 'r') as file: 
        content = file.read().replace("[NAME]", name)
        
    return content

    

def send_birthday_mail(name, email):
    message = get_message(name)
    print(message)
    print(email)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pswd)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday!!\n\n{message}")

for bday in b_dict.keys():
    if now.day == bday.day and now.month == bday.month:
        bday_info = b_dict[bday]
        print(bday_info["name"])
        send_birthday_mail(bday_info["name"], bday_info["email"])
        







