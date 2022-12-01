print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

bill_with_tip = round((tip/100 * bill + bill) / people,2)
print(f"Everyone should pay ${bill_with_tip}")