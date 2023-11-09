# 955A - Feed the cat
# This is a solution to codeforces problem 955A - Feed the cat

hh, mm = map(int, input().split())
h, d, c, n = map(int, input().split())
currMinCost = 0
temp = 0
if h % n == 0:
    temp = h // n
else:
    temp = h // n + 1
temp = temp * c
currMinCost = temp
if hh >= 20 and hh <= 23:
    pct20 = temp/5
    currMinCost = temp - pct20
else:
    r = 0
    totalMins = 0
    if hh == 19:
        totalMins = 60 - mm
    else:
        totalMins = (20 - hh - 1) * 60 + (60 - mm)
    hunger = h + totalMins*d
    if hunger % n == 0:
        r = hunger // n
    else:
        r = hunger // n + 1
    r = r * c
    pct20 = r/5
    r = r - pct20
    if r < currMinCost:
        currMinCost = r
currMinCost = "{:.4f}".format(currMinCost)
print(currMinCost)
