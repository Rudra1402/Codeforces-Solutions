// 1551A---Poylcarp-and-Coins
// This is a solution to codeforces problem 1551A - Polycarp and Coins

#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, c1 = 0, c2 = 0, mod, test;
    cin >> test;
    for (int i = 0; i < test; i++)
    {
        cin >> n;
        mod = n % 3;
        c1 = n / 3;
        c2 = c1;
        if (mod == 0)
            cout << c1 << " " << c2 << "\n";
        if (mod == 1)
            cout << ++c1 << " " << c2 << "\n";
        if (mod == 2)
            cout << c1 << " " << ++c2 << "\n";
    }
    return 0;
}
