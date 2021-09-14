// 1183A - Nearest Interesting Number
// This is a solution to codeforces problem 1183A - Nearest Interesting Number

#include<bits/stdc++.h>
using namespace std;
int calcSum(int s)
{
    int sum = 0;
    while (s > 0)
    {
        sum += (s % 10);
        s /= 10;
    }
    return sum;
}
int main()
{
    int a;
    cin >> a;
    for (int i = 0;; i++)
    {
        if (calcSum(a+i) % 4 == 0)
        {
            cout << a + i;
            break;
        }
        else
            continue;
    }
return 0;
}
