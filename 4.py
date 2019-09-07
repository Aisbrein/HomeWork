def checkIfPolyndrom(number):
    stringNumber = str(number)
    i = len(str(number))
    if i % 2 == 0:
        firstHalf = stringNumber[0:int((i / 2))]
        secondHalf = stringNumber[int((i / 2)):i]
    else:
        firstHalf = stringNumber[0:int((i / 2-1))]
        secondHalf = stringNumber[int((i / 2+1)):i]
    if firstHalf == ''.join(reversed(secondHalf)):
        return True
    else:
        return False

firstDigit = 100
max = 0
while (firstDigit <= 999):
    secondDigit = 100
    while (secondDigit <= 999):
        if checkIfPolyndrom(firstDigit * secondDigit):
            if firstDigit * secondDigit > max:
                max = firstDigit * secondDigit
                digit1 = firstDigit
                digit2 = secondDigit
        secondDigit += 1
    firstDigit +=1
print(max)
print(digit1)
print(digit2)