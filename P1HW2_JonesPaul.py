# Paul Jones
# 8/1/2024
# P1HW2_JonesPaul
# Travel Expenses

# Outline

print("This program calculates and displays travel expenses")
print()
budget = int(input("Enter Budget: "))
print()
location = (input("Enter your travel destination: "))
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
accom = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()
total = int((budget) - (gas + accom + food))

# Travel expenses/results

print()
print("---------------Travel Expenses--------------")
print(f"Location: {location}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accomodation: {accom}")
print(f"Food: {food}")
print()
print(f"Remaining Balance: {total}")
