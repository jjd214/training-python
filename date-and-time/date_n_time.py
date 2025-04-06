from datetime import date
from datetime import datetime


# today = date.today()
# print(f"The date today is {today}")

# # Date (today) components
# print(f"Date components: {today.month} {today.day} {today.year}")

# print(f"Today weekday is {today.weekday()}")

# days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# print(days[today.weekday()])     


# Date time

today = datetime.now()

print(f"The date and time today is {today}")

# Date and time components


# Get the current time
time = datetime.time(today)

print(f"The time today is {time}")