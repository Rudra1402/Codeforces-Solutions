// 158B - Taxi
// This is a solution to codeforces problem 158B - Taxi

    #include <bits/stdc++.h>
    using namespace std;
    long long a[100005];
    int main()
    {
        int i, n, ct1, ct2, ct3, ct4, taxiCount = 0, div = 1, mod;
        cin >> n;
        for (i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        ct1 = count(a, a + n, 1);
        ct2 = count(a, a + n, 2);
        ct3 = count(a, a + n, 3);
        ct4 = count(a, a + n, 4);
        taxiCount += ct4;
        if (ct2 % 2 == 0)
        {
            taxiCount += ct2 / 2;
            if (ct1 == ct3)
                taxiCount += ct1;
            else if (ct3 > ct1)
            {
                taxiCount += ct1;
                ct3 -= ct1;
                taxiCount += ct3;
            }
            else
            {
                taxiCount += ct3;
                ct1 -= ct3;
                if (ct1 % 4 == 0)
                    taxiCount += (ct1 / 4);
                else
                    taxiCount += (ct1 / 4) + 1;
            }
        }
        else
        {
            taxiCount += ct2 / 2;
            if (ct1 == ct3)
                taxiCount += ct1 + 1;
            else if (ct3 > ct1)
            {
                taxiCount += ct1 + 1;
                ct3 -= ct1;
                taxiCount += ct3;
            }
            else
            {
                taxiCount += ct3;
                ct1 -= ct3;
                mod = ct1 % 4;
                div = ct1 / 4;
                if (mod <= 2)
                    taxiCount += div + 1;
                else
                    taxiCount += div + 2;
            }
        }
        cout << taxiCount;
        return 0;
    }
