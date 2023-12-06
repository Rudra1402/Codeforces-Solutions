// 581A - Vasya the Hipster
// This is a solution to codeforces problem 581A - Vasya the Hipster

    #include <bits/stdc++.h>
    using namespace std;
    int main()
    {
        int a, b, diffSocks = 0, sameSocks = 0;
        cin >> a >> b;
        if(a==b)
            diffSocks = a;
        else if (a > b)
        {
            diffSocks = b;
            a = a - b;
            if (a > 1)
                sameSocks = a / 2;
            else
                sameSocks = 0;
        }
        else
        {
            diffSocks = a;
            b = b - a;
            if (b > 1)
                sameSocks = b / 2;
            else
                sameSocks = 0;
        }
        cout<<diffSocks<<" "<<sameSocks;
        return 0;
    }
