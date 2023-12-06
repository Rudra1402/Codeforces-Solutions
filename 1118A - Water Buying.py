# 1118A - Water Buying
# This is a solution to codeforces problem 1118A - Water Buying

q = int(input())
for i in range(q):
    n, a, b = map(int, input().split())
    totalBurles = 0
    if n == 1:
        print(a)
    else:
        if b/2 <= a:
            totalBurles += int(n/2)*b
            n -= int(n/2)*2
            totalBurles += n*a
        else:
            totalBurles += n*a
        print(totalBurles)
