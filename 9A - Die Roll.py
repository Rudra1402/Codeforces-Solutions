# 9A - Die Roll
# This is a solution to codeforces problem 9A - Die Roll

def calculate_hcf(x, y):  
    for i in range(1,x + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    return hcf


Yakko, Wakko = map(int, input().split())
if Yakko > Wakko:
    p = 6 - Yakko + 1
    if 6 % p == 0:
        prob = "1/" + str(int(6/p))
        print(prob)
    else:
        hcf = calculate_hcf(p, 6)
        if hcf == 1:
            prob = str(p) + "/" + str(6)
            print(prob)
        else:
            prob = str(int(p/hcf)) + "/" + str(int(6/hcf))
            print(prob)
else:
    p = 6 - Wakko + 1
    if 6 % p == 0:
        prob = "1/" + str(int(6/p))
        print(prob)
    else:
        hcf = calculate_hcf(p, 6)
        if hcf == 1:
            prob = str(p) + "/" + str(6)
            print(prob)
        else:
            prob = str(int(p/hcf)) + "/" + str(int(6/hcf))
            print(prob)
