def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

result_2024 = is_leap_year(2024)
print(f"2024 is a leap year: {result_2024}")

result_2100 = is_leap_year(2100)
print(f"2100 is a leap year: {result_2100}")