📊 Rent Calculator (Python)

A simple and beginner-friendly Python program that calculates how much each person needs to pay by splitting total living expenses.



🚀 Features

 Calculates total expenses including:

   🏠 Rent
   🍔 Food expenses
   ⚡ Electricity bill
 Splits the total cost among roommates
 Easy to understand and beginner-friendly code
 Uses basic Python concepts (input, variables, arithmetic)



🧮 How It Works

1. User enters:

    Total rent
    Food expenses
    Electricity units consumed
    Charge per unit
    Number of people

2. Program calculates:

    Electricity bill = `units × charge per unit`
    Total expense = `rent + food + electricity`
    Per person share = `total ÷ persons`


💻 Code Example


rent = float(input("Enter total rent: "))
food = float(input("Enter food expense: "))
electricity_units = float(input("Enter electricity units used: "))
charge_per_unit = float(input("Enter charge per unit: "))
persons = int(input("Enter number of persons: "))

electricity_bill = electricity_units * charge_per_unit
total = rent + food + electricity_bill
per_person = total / persons

print("Each person has to pay:", round(per_person, 2))


📌 Requirements

 Python 3.x



🎯 Future Improvements

 Add error handling (invalid input, zero division)
 Convert into GUI application (Tkinter)
 Add monthly expense tracking
 Build web version using Flask

 
