# Paul Jones
# 7/15/2024
# P3LAB
# Currency Efficiency

# Determine amount



max_amount = float(input("Enter the amount of money as a float: $"))
dollars = (1-999)
dimes = (.10, .20, .30, .40, .50, .60, .70, .80, .90)
pennies = (.01, .02, .03, .04, .06, .07, .09)
nickles = (.05, .15, .35, .45, .55, .65, .85, .95)
quarters = (.25, .50, .75)

max_setupdo = ({dollars} // (1))
max_setupdi = ({dimes} // (.10))
max_setupp = ({pennies} // (.01))
max_setupn = ({nickels} // (.05))
max_setupq = ({quarters} // (.25))
min_value = (0)

# Calculations

dollars = (max_setupdo) // (1)
dimes = (max_setupdi) // (.10)
pennies = (max_setupp) // (.01)
nickles = (max_setupn) // (.05)
quarters = (max_setupq) // (.25)

# Input

print(f"{min_value}")
print(f"{dollars}")
print(f"{quarters}")
print(f"{dimes}")
print(f"{nickles}")
print(f"{pennies}")

# Results

if min_value:
    print('No change')

if dollars > 1:
    print('Dollars')
else:
    print('Dollar')

if dimes > 1:
    print('Dimes')
else:
    print('Dime')

if pennies > 1:
    print('Pennies')
else:
    print('Penny')

if nickels > 1:
    print('Nickels')
else:
    print('Nickel')

if quarters > 1:
    print('Quarters')
else:
    print('Quarter')
