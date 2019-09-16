sum = 0
i = 0
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

def numberToBinar(number):
    stringNumber = ""
    while number != 0:
        stringNumber += str(number % 2)
        number = number//2
    if number == 1:
        stringNumber += "1"
    if number == 0:
        stringNumber += "0"
    return "".join(reversed(stringNumber))


while i < 12:
    print(numberToBinar(i))
    if checkIfPolyndrom(i):
        if checkIfPolyndrom(numberToBinar(i)):
            sum += 1
    i += 1
print(sum)