# 1560B - Who's Opposite
# This is a solution to codeforces problem 1560B - Who's Opposite

test = int(input())
for i in range(test):
    a, b, c = map(int, input().split())
    n = 2*(a - b)
    diff = a - b
    if n < 0:
        n = -n
    if diff < 0:
        diff = -diff
    if c > n or a > n or b > n:
        print(-1)
    else:
        if c <= n/2:
            print(int(n/2) + c)
        else:
            print(c - int(n/2))
