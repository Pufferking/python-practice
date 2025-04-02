from datetime import datetime
import pandas as pd
import smtplib
import random

# Email credentials
my_email = "test621094268@gmail.com"
password = "eaurquahylwrwobh"

# Read the birthday data
data = pd.read_csv("birthdays.csv")

# Get today's date as a tuple (month, day)
today = datetime.now()
today_tuple = (today.month, today.day)

# Select a random letter template
random_no = random.randint(1, 3)

# Create a dictionary with (month, day) as keys and row data as values
birthdays_dict = {(row.month, row.day): row for (_, row) in data.iterrows()}

# Check if today matches any birthday
if today_tuple in birthdays_dict:
    # Extract the name of the birthday person
    birthday_person = birthdays_dict[today_tuple]["name"]

    # Read a random letter template and personalize it
    with open(f"./letter_templates/letter_{random_no}.txt") as letter:
        final_letter = letter.read().replace("[NAME]", birthday_person)

    # Send an email with the birthday letter
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_dict[today_tuple]["email"],
            msg=f"Subject:Happy Birthday!\n\n{final_letter}"
        )