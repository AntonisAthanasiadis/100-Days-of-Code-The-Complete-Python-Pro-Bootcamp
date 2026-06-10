cubes = {x: x**3 for x in range(1, 6)}
print(cubes)

prices = {"laptop": 1200, "mouse": 25, "monitor": 300, "cable": 10}
discounted_expensive_items = {item: price * 0.9 for item, price in prices.items() if price > 100}
print(discounted_expensive_items)