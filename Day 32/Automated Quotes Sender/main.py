import smtplib
import datetime as dt
import random

# Variables
my_email = "johnivanpuayapamerica@gmail.com"
password = "xznqqbtxetfshwuy"

# Load the Quotes
with open("Day 32\Automated Quotes Sender\quotes.txt") as file:
    quotes = file.readlines()

# Choose a random qoute
message = f"Subject: Monday Motivational Quote\n\n{random.choice(quotes)}"

# Check the Date
date_now = dt.datetime.now()

if date_now.weekday() == 0:
    # Send the Email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="johnivanpuayap@gmail.com", msg=message)

        