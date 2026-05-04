#range function in for loop

#print 1-10
for number in range(1, 11):
    print(number)

#print 1-10 in steps of 3
for number in range(1, 11, 3):
    print(number)

#add all the numbers to 100
total = 0
for number in range(1, 101):
    total += number
print(total)
