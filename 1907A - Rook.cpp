// 1907A - Rook
// Codeforces Round 913 (Div. 3)
// This is a solution to codeforces problem 1907A - Rook

#include <iostream>
#include <string.h>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t > 0)
    {
        vector<pair<char, int>> positions;
        string initialPos;
        cin >> initialPos;
        char colNum = initialPos[0], rowNum = initialPos[1];
        int rowStrToNum = rowNum - '0';
        int temp = rowStrToNum;
        while (temp > 0)
        {
            temp--;
            if (temp < 1)
            {
                break;
            }
            positions.push_back({colNum, temp});
        }
        temp = rowStrToNum;
        while (temp < 9)
        {
            temp++;
            if (temp > 8)
            {
                break;
            }
            positions.push_back({colNum, temp});
        }
        char tempChar = colNum;
        while (tempChar >= 'a')
        {
            tempChar--;
            if (tempChar < 'a')
            {
                break;
            }
            positions.push_back({tempChar, rowStrToNum});
        }
        tempChar = colNum;
        while (tempChar <= 'h')
        {
            tempChar++;
            if (tempChar > 'h')
            {
                break;
            }
            positions.push_back({tempChar, rowStrToNum});
        }
        for (pair<char, int> pos : positions)
        {
            cout << pos.first << pos.second << endl;
        }
        t--;
    }
    return 0;
}
