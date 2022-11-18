# 1040B - Shashlik Cooking
# This is a solution to codeforces problem 1040B - Shashlik Cooking

n, k = map(int, input().split())
kClosest = 2*k + 1
if kClosest >= n:
    print(1)
    print(int(n/2)+1)
else:
    if n % kClosest == 0:
        l = int(n/kClosest)
    else:
        l = int(n/kClosest)+1
    print(l)
    if kClosest > n % kClosest > k or n % kClosest == 0:
        for i in range(l):
            print((k+1) + i*kClosest, end=" ")
    else:
        for i in range(l):
            print(1 + i*kClosest, end=" ")
