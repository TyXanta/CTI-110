#Paul Jones
#7/15/2024
#P2HW2
#Module Test List

module_grade = []

#Test grade list

module_1 = float(input("Enter grade for Module 1: "))
module_grade.append(module_1)
module_2 = float(input("Enter grade for Module 2: "))
module_grade.append(module_2)
module_3 = float(input("Enter grade for Module 3: "))
module_grade.append(module_3)
module_4 = float(input("Enter grade for Module 4: "))
module_grade.append(module_4)
module_5 = float(input("Enter grade for Module 5: "))
module_grade.append(module_5)
module_6 = float(input("Enter grade for Module 6: "))
module_grade.append(module_6)

#Results

min_grade = min(module_grade)
max_grade = max(module_grade)
total = sum(module_grade)
av_grade = (module_1 + module_2 + module_3 + module_4 + module_5 + module_6) / 6

print()
print(f"-----------Results-----------")
print(f"Lowest Grade:   {min_grade}")
print(f"Highest Grade:  {max_grade}")

print(f"Sum of Grades:  {total}")
print(f"Average:        {av_grade:.2f}")
print(f"---------------------------------")
