# 714A - Meeting of Old Friends
# This is a solution to codeforces problem 714A - Meeting of Old Friends

l1, l2, r1, r2, k = map(int, input().split())
if r1 < l1 and r2 < l1:
    print(0)
else:
    if r1 <= l2:
        if r1 <= l1:
            if r2 <= l2:
                if l1 <= k <= r2:
                    print(r2-l1)
                else:
                    print(r2-l1+1)
            else:
                if l1 <= k <= l2:
                    print(l2 - l1)
                else:
                    print(l2 - l1 + 1)
        else:
            if r2 <= l2:
                if r1 <= k <= r2:
                    print(r2-r1)
                else:
                    print(r2-r1+1)
            else:
                if r1 <= k <= l2:
                    print(l2-r1)
                else:
                    print(l2-r1+1)
    else:
        print(0)
