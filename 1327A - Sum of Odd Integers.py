# 1327A - Sum of Odd Integers
# This is a solution to codeforces problem 1327A - Sum of Odd Integers

import math

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if (n % 2 == 0 and k % 2 != 0) or (n % 2 != 0 and k % 2 == 0):
        print("NO")
    else:
        sqrt_of_n = int(math.sqrt(n))
        if k > sqrt_of_n:
            print("NO")
        else:
            print("YES")
