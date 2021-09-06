# 50B - Choosing Symbol Pairs
# This is a solution to codeforces problem 50B - Choosing Symbol Pairs

pairs = 0
s = input()
sList = []
chkList = []
chkCountList = []
for i in s:
    if i not in chkList:
        chkList.append(i)
        chkCountList.append(s.count(i))
    else:
        pass
for i in chkCountList:
    if i > 1:
        pairs += (i*i)
    else:
        pairs += 1
print(pairs)
