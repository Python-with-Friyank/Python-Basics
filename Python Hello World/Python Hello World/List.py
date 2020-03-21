number = [2,3,5,7,9,10]
largestNumber = 0
for item in number:
    if item > largestNumber:
        largestNumber = item
print(f'Largest Number in List is {largestNumber}')