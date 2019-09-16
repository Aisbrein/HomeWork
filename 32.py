multiplier = 0
multiplicand = 0
product = 0
i = 0
j = 0
sum = 0
def chekkk(resultAsString):
    k = 0
    while k <= len(resultAsString)-1:
        l = k + 1
        while l <= len(resultAsString)-2:
            if resultAsString[k] == resultAsString[l]:
                return False
            l += 1
        k += 1
    return True

def check(arg1,arg2):
    result = arg1*arg2
    resultAsString = str(arg1) + str(arg2) + str(result)
    if len(resultAsString) == 9:
        if chekkk(resultAsString):
            return True
        else:
            return False
    else:
        return False

while i <= 1000:
    j = 0
    while j <= 1000:
        if check(i,j)==True:
            sum += i * j
        j += 1
    i += 1
print(sum/2)