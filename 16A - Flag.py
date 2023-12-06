# 16A - Flag
# This is a solution to codeforces problem 16A - Flag

def sameChar(ch):
    for i in range(1, len(ch)):
        if ch[0] != ch[i]:
            return False
    return True    


flg = False
n, m = map(int, input().split())
flagStr = []
for i in range(n):
    hVal = input()
    flagStr.append(hVal)
if len(flagStr) == 1:
    if sameChar(flagStr[0]):
        print("YES")
    else:
        print("NO")
else:
    for i in range(1, len(flagStr)):
        if sameChar(flagStr[0]):
            flg = True
        else:
            flg = False
            break
        if sameChar(flagStr[i]):
            if flagStr[i] == flagStr[i-1]:
                flg = False
                break
            else:
                flg = True
        else:
            flg = False
            break
    if flg:
        print("YES")
    else:
        print("NO")
