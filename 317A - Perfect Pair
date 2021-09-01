// 317A---Perfect-Pair
// This is a solution to codeforces problem 317A - Perfect Pair

#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
int returnOps(ll a1, ll b1, ll m1)
{
    ll ops = 0;
    while (a1 < m1 && b1 < m1)
    {
        if (a1 < b1)
            a1 += b1;
        else if (b1 < a1)
            b1 += a1;
        else if (a1 == b1)
            a1 += b1;
        ++ops;
    }
    return ops;
}
int returnNegOps(ll a1, ll b1, ll m1)
{
    ll ops = 0;
    while (a1 > m1 && b1 > m1)
    {
        if (a1 > b1)
            a1 += b1;
        else if (b1 > a1)
            b1 += a1;
        else if (a1 == b1)
            a1 += b1;
        ++ops;
    }
    return ops;
}
int main()
{
    ll a, b, m, ops = 0, mod, diff;
    cin >> a >> b >> m;
    if (m > 0)
    {
        if (a >= m || b >= m)
            cout << 0;
        else if (a <= 0 && b <= 0)
            cout << -1;
        else if (a < 0 && b > 0 && (-a > b))
        {
            mod = -a % b;
            ops = -a / b;
            a = a + (-a - mod);
            ops += returnOps(a, b, m);
            cout << ops;
        }
        else if (b < 0 && a > 0 && (-b > a))
        {
            mod = -b % a;
            ops = -b / a;
            b = b + (-b - mod);
            ops += returnOps(a, b, m);
            cout << ops;
        }
        else
        {
            ops += returnOps(a, b, m);
            cout << ops;
        }
    }
    else
    {
        if (a >= m || b >= m)
            cout << 0;
        else if (a <= 0 && b <= 0)
            cout << -1;
        else if (a < 0 && b > 0 && (b > -a))
        {
            mod = b % -a;
            ops = b / -a;
            b = b - (b - mod);
            ops += returnNegOps(a, b, m);
            cout << ops;
        }
        else if (b < 0 && a > 0 && (a > -b))
        {
            mod = a % -b;
            ops = a / -b;
            a = a - (a - mod);
            ops += returnNegOps(a, b, m);
            cout << ops;
        }
        else
        {
            ops += returnNegOps(a, b, m);
            cout << ops;
        }
    }
    return 0;
}
