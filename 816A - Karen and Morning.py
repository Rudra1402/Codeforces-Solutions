# 816A - Karen and Morning
# This is a solution to codeforces problem 816A - Karen and Morning

oneList = [6, 7, 8, 9]
oneNo = 3
twoList = [15, 16, 17, 18, 19]
twoNo = 4
time = input()
hhmm = time.split(":")
hh = int(hhmm[0])
mm = int(hhmm[1])
hhInverted = int(hhmm[0][::-1])
if hh < 10:
    incHH = int(str(int(hhmm[0][1]) + 1)[::-1] + '0')
else:
    incHH = int(str(int(hhmm[0]) + 1)[::-1])
if time == time[::-1]:
    print(0)
else:
    if hh == 5 and mm > 50:
        print(4*60 + 61 - mm)
    elif hh >= 6 and hh < 10:
        for i in oneList:
            if hh == i:
                print(60*oneNo + 61 - mm)
                break
            oneNo -= 1
    elif hh >= 15 and hh < 20:
        for i in twoList:
            if hh == i:
                print(60*twoNo + 62 - mm)
                break
            twoNo -= 1
    elif hhInverted > mm:
        print(hhInverted-mm)
    else:
        if hh == 23:
            print(60 - mm)
        
        else:
            print(60 - (mm - incHH))
