# 706A - Beru-Taxi
# This is a solution to codeforces problem 706A - Beru-Taxi

import math
timeList= []
a, b = map(int, input().split())
noOfTaxi = int(input())
for i in range(noOfTaxi):
    xi, yi, vi = map(int, input().split())
    distance = math.sqrt((xi - a) ** 2 + (yi - b) ** 2)
    time = distance / vi
    timeList.append(time)
print(min(timeList))
