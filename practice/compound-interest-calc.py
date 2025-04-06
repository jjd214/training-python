# Challenge 1: Compound interest calculator

principle = 0
rate = 0
time = 0

isTrue = True

while principle == 0:
    principle = float(input("Enter the principle amount: "))

    if principle <= 0:
        print("Principle amount must be greater than 0")
        principle = 0

while rate == 0:
    rate = float(input("Enter the rate of interest: "))

    if rate <= 0:
        print("Rate of interest must be greater than 0")
        rate = 0

while time == 0:
    time = float(input("Enter the time in years: "))

    if time <= 0:
        print("Time must be greater than 0")
        time = 0

total = principle * (1 + rate / 100) ** time
interest = total - principle

print(f"Total amount after {time:.0f} years is: {total:.2f}")
print(f"Interest earned is: {interest:.2f}")