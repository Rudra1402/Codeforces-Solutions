# 884B - Japanese Crosswords Strike Back 
# This is a solution to codeforces problem 884B - Japanese Crosswords Strike Back

n, x = map(int, input().split())
nList = list(map(int, input().split()))

if x-sum(nList) == len(nList) - 1:
    print("YES")
else:
    print("NO")
