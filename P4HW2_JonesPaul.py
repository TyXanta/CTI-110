# Paul Jones
# 7/22/2024
# P4HW2
# Salary

# Dictionary

data_1 = input("Enter employee's name or "Done" to terminate: ")
data_2 = float(input("How many hours did ({data_1}) work? "))
data_3 = float(input("What is {data_1}'s pay rate? "))
Done = end

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
