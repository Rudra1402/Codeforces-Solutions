# 960A - Check the string
# This is a solution to codeforces problem 960A - Check the string

s = input()
temp = []
chkFlag = True
for i in range(len(s)-1):
    if (s[i] == 'b' and s[i+1] == 'a') or (s[i] == 'c' and s[i+1] == 'b') or (s[i] == 'c' and s[i+1] == 'a'):
        chkFlag = False
    if s[i] not in temp:
        temp.append(s[i])
if 'c' not in temp and s[len(s)-1] == 'c':
    temp.append('c')
if chkFlag == False:
    print("NO")
elif temp == ['a', 'b', 'c']:
    aCount = s.count('a')
    bCount = s.count('b')
    cCount = s.count('c')
    if aCount == cCount or bCount == cCount:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
