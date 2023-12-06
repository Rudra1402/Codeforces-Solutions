# 19A - World Football Cup
# This is a solution to codeforces problem 19A - World Football Cup

n = int(input())

scores = {}
for i in range(n):
    tName = input()
    scores[tName] = [0, 0, 0]

desLen = int(n*(n-1)/2)
for i in range(desLen):
    gameDes = input()
    sepDes = gameDes.split(' ')
    sepT = sepDes[0].split('-')
    sepS = sepDes[1].split(':')

    scores[sepT[0]][2] = scores[sepT[0]][2] + int(sepS[0])
    scores[sepT[1]][2] = scores[sepT[1]][2] + int(sepS[1])

    if int(sepS[0]) > int(sepS[1]):
        scores[sepT[0]][0] = scores[sepT[0]][0] + 3

        scores[sepT[0]][1] = scores[sepT[0]][1] + \
            (int(sepS[0]) - int(sepS[1]))

        scores[sepT[1]][1] = scores[sepT[1]][1] + \
            (int(sepS[1]) - int(sepS[0]))
    elif int(sepS[0]) < int(sepS[1]):
        scores[sepT[1]][0] = scores[sepT[1]][0] + 3

        scores[sepT[1]][1] = scores[sepT[1]][1] + \
            (int(sepS[1]) - int(sepS[0]))

        scores[sepT[0]][1] = scores[sepT[0]][1] + \
            (int(sepS[0]) - int(sepS[1]))
    else:
        scores[sepT[0]][0] = scores[sepT[0]][0] + 1

        scores[sepT[1]][0] = scores[sepT[1]][0] + 1

valArr = sorted(scores.values(), reverse=True)
keyArr = []

for i in range(0, int(len(valArr)/2)):
    keyArr.append(list(scores.keys())[
                  list(scores.values()).index(valArr[i])])

for i in sorted(keyArr):
    print(i)
