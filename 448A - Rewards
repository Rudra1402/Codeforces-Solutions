# 448A - Rewards
# This is a solution to codeforces problem 448A - Rewards
    
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
n = int(input())
sumTrophy = a1 + a2 + a3
sumMedal = b1 + b2 + b3
mod1 = int(sumTrophy/5)
mod2 = sumTrophy % 5
if mod2 == 0:
    n = n - mod1
else:
    n = n - (mod1 + 1)
mod3 = int(sumMedal/10)
mod4 = sumMedal % 10
if mod4 == 0:
    n = n - mod3
else:
    n = n - (mod3 + 1)
if n >= 0:
    print('YES')
else:
    print('NO')
