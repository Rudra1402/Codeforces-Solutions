// 839A - Arya and Bran
// This is a solution to codeforces problem 839A - Arya and Bran

    #include <bits/stdc++.h>
    using namespace std;
    long long a[100];
    int main()
    {
        int n, k, sum = 0, candySum = 0, extraCandies = 0, i, index;
        cin >> n >> k;
        for (i = 1; i < n + 1; i++)
        {
            cin >> a[i];
        }
        sum = accumulate(a, a + (n + 1), sum);
        if (sum < k || (n * 8) < k)
            cout << -1;
        else
        {
            for (i = 1; i < n + 1; i++)
            {
                if (candySum < k)
                {
                    index = i;
                    if (a[i] <= 8)
                    {
                        if ((8 - a[i]) < extraCandies)
                        {
                            candySum += a[i] + (8 - a[i]);
                            extraCandies -= (8 - a[i]);
                        }
                        else
                        {
                            candySum += a[i] + extraCandies;
                            extraCandies = 0;
                        }
                    }
                    else
                    {
                        candySum += 8;
                        extraCandies += a[i] - 8;
                    }
                }
            }
            if(candySum < k)
                cout<<-1;
            else
                cout<<index;
        }
        return 0;
    }
