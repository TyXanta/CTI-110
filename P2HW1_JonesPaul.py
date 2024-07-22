# Paul Jones
# 7/20/2024
# P2HW1
# Edit and Enhance Existing Programs

print("This program calculates and displays travel expenses")

# Setup questions

budget = float(input("Enter Budget: "))
location = (input("Enter your travel destination: "))
gas = float(input("How much do you think you will spend on gas? "))
accom = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))
total = (budget) - (gas + accom + food)

# Travel expenses/results

print()
print("---------------Travel Expenses--------------")
print(f"Location:           {location}")
print(f"Initial Budget:     ${budget:.2f}")
print(f"Fuel:               ${gas:.2f}")
print(f"Accomodation:       ${accom:.2f}")
print(f"Food:               ${food:.2f}")
print("--------------------------------------------")
print()

print(f"Remaining Balance:  ${total:.2f}")
