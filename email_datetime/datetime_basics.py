from datetime import datetime

current_time = datetime.now()

print("Current Date and Time:")
print(current_time)

formatted_time = current_time.strftime("%A, %B %d, %Y at %I:%M %p")
print("\nFormatted Date and Time:")
print(formatted_time)