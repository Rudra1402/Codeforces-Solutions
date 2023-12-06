# 1154B - Make Them Equal
# This is a solution to codeforces problem 1154B - Make Them Equal

flag = True
n = int(input())
nList = list(map(int, input().split()))
chkList = []
nList.sort()
for i in nList:
    if i not in chkList:
        chkList.append(i)
    else:
        pass
if len(chkList) == 1:
    print(0)
elif len(chkList) == 2:
    diff = chkList[1] - chkList[0]
    if diff % 2 == 0:
        print(int(diff/2))
    else:
        print(diff)
elif len(chkList) > 3:
    print(-1)
else:
    diff = chkList[1] - chkList[0]
    for i in range(n-1):
        if nList[i + 1] - nList[i] == diff or nList[i + 1] - nList[i] == 0:
            flag = True
        else:
            flag= False
            break
    if flag == True:
        print(diff)
    else:
        print(-1)
