print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_number = int(input("How many people to split the bill? "))
per_person_value = round(total_bill * ((tip_percent + 100) / 100) / people_number, 2)
print(f'Each person should pay ${"{:.2f}".format(per_person_value)}')

