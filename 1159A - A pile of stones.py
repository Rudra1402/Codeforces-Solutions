# 1159A - A pile of stones
# This is a solution to codeforces problem 1159A - A pile of stones

minimumStones = 0
n = int(input())
addsub = input()
for i in addsub:
    if i == '-' and minimumStones == 0:
        pass
    elif i == '-':
        minimumStones -= 1
    else:
        minimumStones += 1
print(minimumStones)
