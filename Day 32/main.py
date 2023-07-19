import smtplib

my_email = "johnivanpuayapamerica@gmail.com"
password = "xznqqbtxetfshwuy"
message = "Subject: Email Test\n\nThis is a test email"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="johnivanpuayap@gmail.com", msg=message)