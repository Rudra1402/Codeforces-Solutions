# 855A - Tom Riddle's Diary
# This is a solution to codeforces problem 855A - Tom Riddle's Diary

diary = []
n = int(input())
for i in range(n):
    name = input()
    if name not in diary:
        diary.append(name)
        print("NO")
    else:
        print("YES")
