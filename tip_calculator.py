print("Welcome to the Tip Calculator!\n")
print("This program will help you calculate the tip for your meal.\n")
total_bill = float(input("What is the total bill amount? $\n"))
tip_percentage = float(input("What percentage tip would you like to give? (e.g., 15 for 15%) \n"))
tip_amount = (tip_percentage / 100) * total_bill
print(f"The tip amount is ${tip_amount:.2f}.\n")
total_amount = total_bill + tip_amount
print(f"The total amount including the tip is ${total_amount:.2f}.\n")
print("Thank you for using the Tip Calculator!\n")