# 466A - Cheap Travel
# This is a solution to codeforces problem 466A - Cheap Travel

n, m, a, b = map(int, input().split())
minCost = 0
if n >= m:
    if b % m == 0 and m % b == 0:
        print(n)
    else:
        if b/m < a:
            minCost += (n // m) * b
            if n % m != 0:
                if a > b:
                    minCost += b
                else:
                    minCost += (n % m) * a
        else:
            minCost += n * a
        print(minCost)
else:
    if b > n * a:
        print(a)
    else:
        print(b)
