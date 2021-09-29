# 96A - Football
# This is a solution to codeforces problem 96A - Football

ct = 1
flg = False
position = input()
for i in range(len(position) - 1):
    if position[i] == position[i+1]:
        ct += 1
        if ct == 7:
            flg = True
            break
    else:
        ct = 1
if flg:
    print("YES")
else:
    print("NO")
