// 1907B - YetnotherrokenKeoard
// This is a solution to codeforces problem 1907B - YetnotherrokenKeoard

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    stack<pair<char, int>> uCase;
    stack<pair<char, int>> lCase;
    int t;
    cin >> t;
    while (t > 0)
    {
        string s;
        cin >> s;
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] == 'b')
            {
                if (!lCase.empty())
                {
                    lCase.pop();
                }
            }
            else if (s[i] == 'B')
            {
                if (!uCase.empty())
                {
                    uCase.pop();
                }
            }
            else if (islower(s[i]))
            {
                lCase.push({s[i], i});
            }
            else if (isupper(s[i]))
            {
                uCase.push({s[i], i});
            }
        }
        vector<pair<char, int>> combined;
        while (!lCase.empty())
        {
            combined.push_back(lCase.top());
            lCase.pop();
        }
        while (!uCase.empty())
        {
            combined.push_back(uCase.top());
            uCase.pop();
        }
        sort(combined.begin(), combined.end(), [](const pair<char, int> &a, const pair<char, int> &b)
             { return a.second < b.second; });

        for (const auto &p : combined)
        {
            cout << p.first;
        }
        cout << endl;

        t--;
    }
    return 0;
}
