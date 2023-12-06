// 467A---George-and-Accommodation
// This is a solution for codeforces problem 467A - George and Accomodation.
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test,ct=0;
    cin>>test;
    while(test--)
    {
        int p,q;
        cin>>p>>q;
        if(q-p>=2)
            ct++;
    }
    cout<<ct;
}
