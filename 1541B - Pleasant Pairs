// 1541B - Pleasant Pairs
// This is a solution to codeforces problem 1541B - Pleasant Pairs

#include<bits/stdc++.h>
using namespace std;
long long arr[200005];
int main()
{
    int i,j,k,pairs=0,n,test;
    cin>>test;
    for(k=0; k<test; k++)
    {
        pairs=0;
        cin>>n;
        for(i=1; i<n+1; i++)
        {
            cin>>arr[i];
        }
        for(i=1; i<n+1; i++)
        {
            for(j=arr[i]-i;j<n+1;j=j+arr[i])
            {
                if(i<j && arr[i]*arr[j]==i+j)
                    pairs++;
            }
        }
        cout<<pairs<<"\n";
    }
}
