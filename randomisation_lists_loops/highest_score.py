student_scores = [140, 145, 121, 144, 167, 134, 111]

#Replicate this with for loop print(max(student_scores))
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
        print(f"New high score: {high_score}")

print(f"The highest score in the list is {high_score}")