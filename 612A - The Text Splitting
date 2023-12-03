// 612A - The Text Splitting
// This is a solution to codeforces problem 612A - The Text Splitting

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, p, q;
    cin >> n >> p >> q;
    string s;
    cin >> s;
    int sLen = s.size();
    int splitCount;
    if (n == p + q)
    {
        splitCount = 2;
        cout << splitCount << endl;
        cout << s.substr(0, p) << endl;
        cout << s.substr(p, sLen) << endl;
    }
    else
    {
        if (n % p == 0)
        {
            splitCount = int(n / p);
            cout << splitCount << endl;
            for (int i = 0; i < n; i += p)
            {
                cout << s.substr(i, p) << endl;
            }
        }
        else if (n % q == 0)
        {
            splitCount = int(n / q);
            cout << splitCount << endl;
            for (int i = 0; i < n; i += q)
            {
                cout << s.substr(i, q) << endl;
            }
        }
        else
        {
            bool flag = false;
            int count = 0, ct1, ct2;
            for (int i = 0; i * p <= n; i++)
            {
                for (int j = 0; i * p + j * q <= n; j++)
                {
                    if (i * p + j * q == n)
                    {
                        flag = true;
                        ct1 = i;
                        ct2 = j;
                        break;
                    }
                }
            }
            if (flag)
            {
                cout << ct1 + ct2 << endl;
                count = 0;
                for (int i = 0; i < ct1; i++)
                {
                    cout << s.substr(count, p) << endl;
                    count = p * (i + 1);
                }
                for (int i = 0; i < ct2; i++)
                {
                    cout << s.substr(count, q) << endl;
                    count += q;
                }
            }
            else
            {
                cout << -1;
            }
        }
    }
    return 0;
}
