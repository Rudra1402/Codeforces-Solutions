# 725B - Food on the Plane
# This is a solution to codeforces problem 725B - Food on the Plane

seat = input()
rowArr = ['f', 'e', 'd', 'a', 'b', 'c']
rowChar = seat[len(seat) - 1]
rowNum = int(seat[:len(seat) - 1])
totalSeconds = 0
if rowNum % 4 == 0:
    div = rowNum // 4 - 1
else:
    div = rowNum // 4
rowMod = rowNum % 4
totalSeconds += div * 16
if rowMod % 2 == 0:
    totalSeconds = totalSeconds + 7 + rowArr.index(rowChar) + 1
else:
    totalSeconds = totalSeconds + rowArr.index(rowChar) + 1
print(totalSeconds)
