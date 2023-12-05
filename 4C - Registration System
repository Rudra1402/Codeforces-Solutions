// 4C - Registration System
// This is a solution to codeforces problems 4C - Registration System

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    unordered_set<string> s;
    unordered_map<string, int> m;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string ename;
        cin >> ename;
        auto it = s.find(ename);
        if (it == s.end())
        {
            s.insert(ename);
            cout << "OK" << endl;
        }
        else
        {
            m[ename]++;
            cout << ename << m[ename] << endl;
        }
    }
    return 0;
}
