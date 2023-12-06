# 31B - Sysadmin Bob
# This is a solution to codeforces problem 31B - Sysadmin Bob

flag = True
index = 0
emailIDList = []
emailID = input()
eLen = len(emailID)
lastIndex = emailID.rfind('@')
firstIndex = emailID.find('@')
tempEmailID = emailID[0:lastIndex]
secondLastIndex = tempEmailID.rfind('@')
if eLen == 1:
    print("No solution")
elif '@' not in emailID:
    print("No solution")
elif emailID[0] == '@' or emailID[eLen-1] == '@':
    print("No solution")
elif lastIndex == firstIndex:
    print(emailID)
else:
    for i in range(eLen - 2):
        if emailID[i] == '@':
            if (emailID[i] == emailID[i+1] or emailID[i] == emailID[i+2]):
                flag = False
                break
            else:
                if emailID[eLen-2] != '@':
                    if i != lastIndex:
                        emailIDList.append(emailID[index:i+2])
                        index = i+2
                    else:
                        emailIDList.append(emailID[index:eLen])
                        break
                elif emailID[eLen-2] == '@':
                    if i != secondLastIndex:
                        emailIDList.append(emailID[index:i+2])
                        index = i+2
                    else:
                        emailIDList.append(emailID[index:eLen-3])
                        emailIDList.append(emailID[eLen-3:eLen])
                        break
    if flag:
        for i in range(len(emailIDList)):
            if i != len(emailIDList) - 1:
                print(emailIDList[i], end = ",")
            else:
                print(emailIDList[i])
    else:
        print("No solution")
