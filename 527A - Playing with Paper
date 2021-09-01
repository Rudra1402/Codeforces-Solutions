// 527A - Playing with Paper
// This is a solution to codeforces problem 527A - Playing with Paper

#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
int main()
{
    ll a, b, div, mod, ships = 0;
    cin >> a >> b;
    while (a > 0 && b > 0)
    {
        if (a % b == 0)
        {
            ships += (a / b);
            break;
        }
        else if (b % a == 0)
        {
            ships += (b / a);
            break;
        }
        else
        {
            if (a > b)
            {
                mod = a % b;
                div = a / b;
                ships += div;
                a = mod;
            }
            else if (b > a)
            {
                mod = b % a;
                div = b / a;
                ships += div;
                b = mod;
            }
        }
    }
    cout << ships;
    return 0;
}
