# 1221C - Perfect Team
# This is a solution to codeforces problem 1221C - Perfect Team

t = int(input())
for i in range(t):
    c, m, x = map(int, input().split())
    if c == 0 or m == 0:
        print(0)
    elif c <= x or m <= x:
        min_of_c_and_m = min(c, m)
        print(min_of_c_and_m)
    else:
        countTeams = 0
        countTeams += x
        c -= x
        m -= x
        x = 0
        if c > 1 and m > 1:
            if c >= 2*m:
                print(m + countTeams)
            elif m >= 2*c:
                print(c + countTeams)
            elif c == m:
                if c % 3 == 0:
                    print(int(c/3)*2 + countTeams)
                else:
                    if c % 3 == 1:
                        print(int(c/3)*2 + countTeams)
                    else:
                        print(int(c/3)*2 + countTeams + 1)
            else:
                mod_c = c % 3
                mod_m = m % 3
                if mod_c + mod_m >= 3:
                    print(int(c/3) + int(m/3) + countTeams + 1)
                else:
                    print(int(c/3) + int(m/3) + countTeams)
        elif c == 1 and m == 1:
            print(countTeams)
        elif (c == 1 and m > 1) or (m == 1 and c > 1):
            print(countTeams + 1)
