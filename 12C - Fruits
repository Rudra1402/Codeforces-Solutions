# 12C - Fruits
# This is a solution to codeforces problem 12C - Fruits

maximum = 0
minimum = 0
n, m = map(int, input().split())
nList = list(map(int, input().split()))
fruitList = []
chkList = []
fruitCountList = []
for i in range(m):
    fruit = input()
    fruitList.append(fruit)
for i in fruitList:
    if i not in chkList:
        chkList.append(i)
        fruitCountList.append(fruitList.count(i))
    else:
        pass
fruitCountList.sort()
fruitCountList.reverse()
nList.sort()
lenCount = len(fruitCountList)
lenCountnList = len(nList)
for i in range(lenCount):
    minimum += (nList[i] * fruitCountList[i])
    maximum += (nList[lenCountnList - 1 - i] * fruitCountList[i])
print(minimum, maximum)
