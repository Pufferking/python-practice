import smtplib
import datetime as dt
import random

# Email credentials
my_email = "test621094268@gmail.com"
password = "eaurquahylwrwobh"

# Get the current weekday (0 = Monday, 6 = Sunday)
now = dt.datetime.now()
weekday = now.weekday()

# Check if today is Wednesday (weekday 2)
if weekday == 2:
    # Read quotes from the file and pick a random one
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)

    # Send the motivational email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test62109@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )