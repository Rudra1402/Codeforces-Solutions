// 519C---AandBandTeamTraining
// This is a solution to codeforces problem 519C - A and B and Team Training

#include <bits/stdc++.h>
using namespace std;
int main()
{
    int xp, nb, d;
    cin >> xp >> nb;
    if (xp <= 1 && nb <= 1)
        cout << 0;
    else if(nb > ((xp*2)+2))
    {
        cout<<xp;
    }
    else if(xp > ((nb*2)+2))
    {
        cout<<nb;
    }
    else
    {
        d = (xp + nb) / 3;
        cout<<d;
    }
    return 0;
}
