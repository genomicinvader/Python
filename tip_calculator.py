print("Welcome to the Tip Calculator!")
print("This program will help you calculate the tip for your meal.")
total_bill = float(input("What is the total bill amount? $"))
tip_percentage = float(input("What percentage tip would you like to give? (e.g., 15 for 15%) "))
tip_amount = (tip_percentage / 100) * total_bill
print(f"The tip amount is ${tip_amount:.2f}.")
total_amount = total_bill + tip_amount
print(f"The total amount including the tip is ${total_amount:.2f}.")
print("Thank you for using the Tip Calculator!")