# 22A---Second-Order-Statistics
# This is a solution for codeforces problem 22A - Second Order Statistics
ct = 0
seq = int(input())
num = list(map(int, input().split(" ")))
num.sort()
for i in num:
    low = num[0]
    if i == low:
        ct += 1
    elif i > low:
        print(i)
        break
if ct == len(num):
    print("NO")
