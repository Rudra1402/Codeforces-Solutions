# 1973A - Chess For Three

t = int(input())

for i in range(t):
    x,y,z = map(int, input().split())
    if (x+y+z) % 2 == 1:
        print(-1)
    elif x+y <= z:
        print(x+y)
    else:
        ct = 0
        while y != x:
            z -= 1
            y -= 1
            ct += 1
        ct += (x+y+z)//2
        print(ct)
