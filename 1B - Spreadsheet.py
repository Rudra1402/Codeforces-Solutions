# 1B - Spreadsheet

import re


alphabet_dict = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y',
    26: 'Z'
}

n = int(input())
for i in range(n):
    cell = input()
    pattern = r'^R\d+C\d+$'
    isRCformat = bool(re.match(pattern, cell))
    if isRCformat:
        digits = re.findall(r'\d+', cell)
        cellnumbers = [int(d) for d in digits]
        col = cellnumbers[1]
        answer = ""
        while col > 26:
            mod = col % 26
            if mod != 0:
                answer = alphabet_dict[mod] + answer
                col = col // 26
            else:
                answer = 'Z' + answer
                col = (col // 26) - 1
        mod = col % 26
        if mod != 0:
            answer = alphabet_dict[mod] + answer
        else:
            answer = 'Z' + answer
        answer += str(cellnumbers[0])
        print(answer)
    else:
        alphabets = ''.join(char for char in cell if char.isalpha())
        alphabets = alphabets[::-1]
        digits = ''.join(char for char in cell if char.isdigit())
        answer = "R"+str(digits)+"C"
        multiplier = 1
        col = 0
        i = 0
        while i <= len(alphabets)-1:
            keys = [key for key, value in alphabet_dict.items() if value == alphabets[i]]
            col += (keys[0] * multiplier)
            i += 1
            multiplier = multiplier * 26
        answer += str(col)
        print(answer)
