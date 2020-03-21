numbers = [5,2,5,2,2]
print('Without using Python style')
for number in numbers:
    LetterF = ''
    for number1 in range(number):
        LetterF += 'X'
    print(LetterF)
print('Using Python style')
for number in numbers:
    print("X" * number)
