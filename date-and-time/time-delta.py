from datetime import timedelta
from datetime import datetime

today= datetime.now()

print(f"Today is : {today}")
print(f"The date today in one year is {today + timedelta(days=365)}")
print(f"In two weeks and 3 days it will be {today + timedelta(weeks=3, days=3)}")

print(f"The date right now 2 years ago is {today - timedelta(days=620)}")