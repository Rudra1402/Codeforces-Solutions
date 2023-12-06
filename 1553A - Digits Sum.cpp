// 1553A---Digits-Sum
// This is a solution to codeforces problem 1553A - Digits Sum

#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, test;
    cin >> test;
    for (int i = 0; i < test; i++)
    {
        cin >> n;
        if (n % 10 == 9)
            cout << (n / 10) + 1 << "\n";
        else
            cout << n / 10 << "\n";
    }
    return 0;
}
