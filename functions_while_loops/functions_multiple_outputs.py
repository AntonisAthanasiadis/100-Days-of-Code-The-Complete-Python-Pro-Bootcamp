def get_math_results(a, b):
    return a + b, a * b

sum_val, prod_val = get_math_results(10, 5)
print(sum_val, prod_val)

def split_name(full_name):
    parts = full_name.split()
    return parts[0], parts[-1]

first, last = split_name("Jane Doe")
print(first, last)

def get_range(numbers):
    return min(numbers), max(numbers)

low, high = get_range([10, 20, 30, 40, 50])
print(low, high)