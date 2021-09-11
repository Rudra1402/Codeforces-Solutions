# 1475A - Odd Divisor
# This is a solution to codeforces problem 1475A - Odd Divisor
 
 from math import ceil, floor, log2


def chkTwoPower(num):
    if ceil(log2(num)) == floor(log2(num)):
        return True
    else:
        return False


nList = []
test = int(input())
for i in range(test):
    n = int(input())
    nList.append(n)
for i in nList:
    if chkTwoPower(i):
        print("NO")
    else:
        print("YES")
