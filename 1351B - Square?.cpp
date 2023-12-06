// 1351B---Square?
// This is a solution to codeforces problem 1351B - Square?

    #include <bits/stdc++.h>
    using namespace std;
    int main()
    {
        int test, a, b, c, d, sqArea, sqRoot, max1, max2, min1, min2;
        cin >> test;
        for (int i = 0; i < test; i++)
        {
            cin >> a >> b;
            cin >> c >> d;
            max1 = std::max(a,b);
            max2 = std::max(c,d);
            min1 = std::min(a,b);
            min2 = std::min(c,d);
            sqArea = (a * b) + (c * d);
            sqRoot = sqrt(sqArea);
            if (sqRoot * sqRoot == sqArea && max1 == max2 && max1 == min1 + min2)
                cout<<"YES\n";
            else
                cout << "NO\n";
        }
        return 0;
    }
