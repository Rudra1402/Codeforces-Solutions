// 1132B - Discounts
// This is a solution to codeforces problem 1132B - Discounts

#include<bits/stdc++.h>
using namespace std;
long long arr[300005];
int main()
{
    int nBars,qBars,qVal,i,j;
    long long sum=0;
    cin>>nBars;
    for(i=0;i<nBars;i++)
    {
        cin>>arr[i];
    }
    sort(arr,arr+nBars);
    for(i=0;i<nBars;i++)
    {
        sum += arr[i];
    }
    cin>>qBars;
    for(j=0;j<qBars;j++)
    {
        cin>>qVal;
        cout<<sum - arr[nBars-qVal]<<"\n";
    }
    return 0;
}
