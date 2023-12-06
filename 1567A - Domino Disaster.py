# 1567A - Domino Disaster
# This is a solution to codeforces problem 1567A - Domino Disaster

splitList = []
t = int(input())
for i in range(t):
    newStr = ""
    s = int(input())
    n = input()
    splitList = list(n)
    for j in splitList:
        if j == 'U':
            newStr += 'D'
        elif j == 'D':
            newStr += 'U'
        else:
            newStr += j
    print(newStr)
