# Rent Calculator - Beginner Friendly

# Taking inputs from the user
rent = int(input("Enter total rent of the flat/hostel: "))
food = int(input("Enter total food expense: "))
electricity_units = int(input("Enter electricity units consumed: "))
charge_per_unit = float(input("Enter charge per unit: "))
persons = int(input("Enter number of persons living: "))

# Calculating electricity bill
electricity_bill = electricity_units * charge_per_unit

# Calculating total expense
total_expense = rent + food + electricity_bill

# Cost per person
per_person = total_expense / persons

# Output
print("\n----- Expense Summary -----")
print(f"Total Rent: {rent}")
print(f"Food Expense: {food}")
print(f"Electricity Bill: {electricity_bill}")
print(f"Total Expense: {total_expense}")
print(f"Each person should pay: {round(per_person, 2)}")