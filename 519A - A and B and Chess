// 519A---A-and-B-and-Chess
// This is a solution to codeforces problem 519A - A and B and Chess
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int i, j, white = 0, black = 0;
    char c[8][8];
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            cin >> c[i][j];
        }
    }
    for (i = 0; i < 8; i++)
    {
        for (j = 0; j < 8; j++)
        {
            if (c[i][j] == 'Q')
                white += 9;
            else if (c[i][j] == 'R')
                white += 5;
            else if (c[i][j] == 'B' || c[i][j] == 'N')
                white += 3;
            else if (c[i][j] == 'P')
                white += 1;
            else if (c[i][j] == 'q')
                black += 9;
            else if (c[i][j] == 'r')
                black += 5;
            else if (c[i][j] == 'b' || c[i][j] == 'n')
                black += 3;
            else if (c[i][j] == 'p')
                black += 1;
            else
                continue;
        }
    }
    if (white > black)
        cout << "White";
    else if (black > white)
        cout << "Black";
    else
        cout << "Draw";
    return 0;
}
