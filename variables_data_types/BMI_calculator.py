#BMI calculator. Saw the one in the course and added an input
#prompt and value validity checks instead of hardcoded height & weight
#Utilized some of the knowledge that comes later in the course, but I was already familiar with

#First, check height type and value.
while True:
    try:
        height = float(input("Enter your height in meters: "))
        if 0.5 <= height <= 3.0:
            break
        else:
            print("Error: Please enter a realistic height between 0.5m and 3.0")
        break
    except ValueError:
        print("Invalid input height! Please enter a valid float or integer.")

#Then, check weight type and value.
while True:
    try:
        weight = float(input("Enter your weight: "))
        if 5 <= weight <= 500:  # Broad range for human safety
            break
        else:
            print("Error: Please enter a realistic weight between 5kg and 500kg.")
        break
    except ValueError:
        print("Invalid input weight! Please enter a valid float or integer.")

#Print BMI. Use a little printing trick to avoid floating point numbers with more than 2 decimal digits
bmi = weight/height**2
print(f"\nYour BMI is: {bmi:.2f}")

#Categorize user based on BMI and print result.
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Health Category: {category}")
