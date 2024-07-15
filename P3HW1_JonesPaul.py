# Paul Jones
# 7/14/2024
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# Determine lowest, highest , sum and average for grades

mod_grade = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
min_grade = min(mod_grade)
max_grade = max(mod_grade)
total = sum(mod_grade)
avg = (mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6) /6

# Results

print()
print("-----------Results-----------")

print(f"Lowest Grade:     {min_grade}")
print(f"Highest Grade:    {max_grade}")
print(f"Sum of Grades:    {total}")
print(f"Average:          {avg:.2f}")

print("---------------------------------")

# Grade display

if avg > 90:
    print('Your grade is: A')

elif avg > 80:
    print('Your grade is: B')

elif avg > 70:
    print('Your grade is: C')

elif avg > 60:
    print('Your grade is: D')

elif avg < 59:
    print('Your grade is: F')
