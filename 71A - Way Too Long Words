# 71A - Way Too Long Words
# This is a solution to codeforces problem 71A - Way Too Long Words

test = int(input())
wordList = []
for i in range(test):
    word = input()
    if len(word) <= 10:
        wordList.append(word)
    else:
        newWord = word[0] + str(len(word) - 2) + word[len(word) - 1]
        wordList.append(newWord)
for i in wordList:
    print(i)
