i = 0
squareSum = 0
sumOfSquares = 0
while i < 100:
    squareSum += i
    sumOfSquares += i ** 2
    i += 1
squareSum **= 2
print(squareSum)
print(sumOfSquares)
difference = squareSum - sumOfSquares
print(difference)