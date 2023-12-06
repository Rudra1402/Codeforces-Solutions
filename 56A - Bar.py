# 56A---Bar
# This is a solution for codeforces problem 56A - Bar
def isfloat(st):
    try:
        int(st)
        return True
    except ValueError:
        return False


nct = 0
ct = 0
test = int(input())
drinks = ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]
while nct < test:
    n = input()
    if isfloat(n):
        if int(n) < 18:
            ct = ct + 1
    else:
        for i in drinks:
            if n == i:
                ct = ct + 1
    nct = nct + 1
print(ct)
