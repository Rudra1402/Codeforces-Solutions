# 12B - Correct Solution?
# This is a solution to codeforces problem 12B - Correct Solution?

Alice = int(input())
Bob = input()
numList = []
numListWithoutZero = []
if Alice == 0 and Bob == '0':
    print("OK")
elif Bob[0] == '0':
    print("WRONG_ANSWER")
else:
    int(Bob)
    MinimumNumber = ""
    while Alice > 0:
        numList.append(Alice%10)
        Alice = int(Alice/10)
    for i in numList:
        if i != 0:
            numListWithoutZero.append(i)
    zeroCount = numList.count(0)
    numListWithoutZero.sort()
    if zeroCount == 0:
        for i in numListWithoutZero:
            MinimumNumber += str(i)
    else:
        MinimumNumber += str(numListWithoutZero[0])
        if len(numListWithoutZero) == 1:
            while zeroCount > 0:
                MinimumNumber += '0'
                zeroCount -= 1
        else:
            for i in range(1, len(numListWithoutZero)):
                while zeroCount > 0:
                    MinimumNumber += '0'
                    zeroCount -= 1
                MinimumNumber += str(numListWithoutZero[i])
    if MinimumNumber == str(Bob):
        print("OK")
    else:
        print("WRONG_ANSWER")
