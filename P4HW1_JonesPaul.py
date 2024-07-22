#Paul Jones
#7/22/2024
#P4HW1
#Score list

scores = []

#Listings

scores = input("How many scores do you want to enter?")


score_1 = input("Enter score #1: ")
score_2 = input("Enter score #2: ")
score_3 = input("Enter score #3: ")

if input <=-1:
    print ("INVALID Score entered!!!!")
    print("Score should be between 0 and 100")
    print()

score_4 = input("Enter score #4: ")
score_5 = input("Enter score #5: ")
score_6 = input("Enter score #6: ")

#Results

min_score = min(score)
max_grade = max(score)
total = sum(score)
av_score = (score_1 + score_2 + score_3 + score_4 + score_5 + score_6) /6

print()
print(f"-----------Results-----------")
print(f"Lowest Grade:   {min_score}")
print(f"Highest Grade:  {score_1, score_2, score_3, score_4, score_5, score_6}")

print(f"Average:        {av_score:.2f}")

# Score display

if avg > 90:
    print('Grade: A')

elif avg > 80:
    print('Grade: B')

elif avg > 70:
    print('Grade: C')

elif avg > 60:
    print('Grade: D')

elif avg < 59:
    print('Grade: F')

print(f"---------------------------------")
