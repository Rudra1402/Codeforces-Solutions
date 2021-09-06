# 1157A - Reachable Numbers
# This is a solution to codeforces problem 1157A - Reachable Numbers

n = int(input())
nList = []
if n == 10:
    nList.append(1)
nList.append(n)
while True:
    n = n + 1
    if n not in nList:
        if n % 10 == 0:
            while n % 10 == 0:
                n = int(n/10)
            if n in nList:
                pass
            else:
                nList.append(n)
        else:
            nList.append(n)
    else:
        break
print(len(nList))
