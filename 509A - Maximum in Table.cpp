// 509A---Maximum-in-Table
// This is a solution to codeforces problem 509A - Maximum in Table

    #include <bits/stdc++.h>
    using namespace std;
    int arr[10][10];
    int main()
    {
        int n, i, j;
        cin >> n;
        for (i = 0; i < n; i++)
        {
            arr[i][0] = 1;
        }
        for (j = 0; j < n; j++)
        {
            arr[0][j] = 1;
        }
        for (i = 0; i < n - 1; i++)
        {
            for (j = 0; j < n - 1; j++)
            {
                arr[i + 1][j + 1] = arr[i][j + 1] + arr[i + 1][j];
            }
        }
        cout << arr[n - 1][n - 1];
        return 0;
    }
