from datetime import datetime

today = datetime.now()


print(today.strftime("The current year today is %Y"))
print(today.strftime("%a, %d, %B, %Y"))