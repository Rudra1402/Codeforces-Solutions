# 946A - Partition
# This is a solution to codeforces problem 946A - Partition

n = int(input())
nList = list(map(int, input().split()))
nList = sorted(nList, reverse=True)
B = []
C = []
for i in nList:
    if i >= 0:
        B.append(i)
    else:
        C.append(i)
print(sum(B) - sum(C))
