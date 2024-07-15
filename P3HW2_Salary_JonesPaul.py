# Paul Jones
# 7/15/2024
# P3HW2
# Salary

# Dictionary

data_1 = input("Enter employee's name: ")
data_2 = float(input("Enter number of hours worked: "))
data_3 = float(input("Enter employee's pay rate: "))

# Calculations

hours_worked = 45
pay_rate = 17.5
overtime = 5
overtime_pay = 131.25
reghour_pay = 700
gross_pay = (overtime_pay + reghour_pay)


# Inputs

print("---------------------------------")
print(f" Employee name:  {data_1}")
print()

#Results
print("Hours Worked   Pay Rate  OverTime    OverTime Pay   RegHour Pay   Gross Pay")
print("------------------------------------------------------------------------------")
print(f'{data_2:<14.1f} {data_3:<9.1f} {overtime:<11.1f} {overtime_pay:<14.2f} ${reghour_pay:<12.2f} ${gross_pay:}')
