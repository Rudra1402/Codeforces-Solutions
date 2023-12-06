# 44A - Indian Summer
# This is a solution to codeforces problem 44A - Indian Summer

miniDict = {}
iSummer = []
chkList = []
test = int(input())
for i in range(test):
    t, c = map(str, input().split())
    miniDict = {t: c}
    iSummer.append(miniDict)
for i in iSummer:
    if i not in chkList:
        chkList.append(i)
print(len(chkList))
