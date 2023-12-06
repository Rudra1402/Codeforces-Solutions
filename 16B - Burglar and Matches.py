# 16B---Burglar-and-Matches
# This is a solution for codeforces problem 16B - Burglar and Matches
res = 0
matchbox = []
matchsticks = []
n, cont = map(int, input().split())
for i in range(cont):
    mb, ms = map(int, input().split())
    matchbox.append(mb)
    matchsticks.append(ms)
tuples = sorted(zip(matchsticks, matchbox))
matchsticks, matchbox = [t[0] for t in tuples], [t[1] for t in tuples]
# print(tuples)
matchbox.reverse()
matchsticks.reverse()
# print(matchsticks, matchbox)
diff = n
for i in range(cont):
    if matchsticks[i] == max(matchsticks) and matchbox[i] < diff:
        res = res + (matchsticks[i]*matchbox[i])
        diff = diff - matchbox[i]
        matchbox[i] = 0
        matchsticks[i] = 0
    else:
        for j in range(cont):
            res = res + (diff*max(matchsticks))
            diff = 0
            break
        break
# print(matchbox, matchsticks)
print(res)
