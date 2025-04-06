# def main():

#     balance = 0

#     while True:
#         print("====== Bank System ======")   
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Show balance")
#         print("4. Exit")
#         print("=========================")

#         ch = input("Enter your choice: ")

#         if ch == "4":
#             print("Thank you for using Bank system.")
#             break
#         elif ch == "1":
#             amount_deposit = float(input("Enter the amount you to deposit: "))
#             balance += amount_deposit
#             print("Deposit success")
#         elif ch == "2":
#             amount_withdraw = float(input("Enter the amount you want to withdraw: "))
#             if amount_withdraw > balance:
#                 print("Insuficient balance!")
#                 print(f"You only have {balance} left!")
#             else:
#                 balance -= amount_withdraw
#                 print("Withdraw success")
#         elif ch == "3":
#             print(f"You have {balance:.2f} balance.")
#         else:
#             print("Invalid input!")

# main()

# if __name__ == "__main__":
#     main()