// 514A---ChewbaccaAndNumber
// This is a solution to codeforces problem 514A - Chewbacca and Number

    #include <bits/stdc++.h>
    using namespace std;
    int main()
    {
        long long num, mod;
        string newMerge = "", newStr, strZero = "0", strNine = "9", strIndexZero;
        cin >> num;
        if (num == 9)
            cout << 9;
        else
        {
            while (num > 0)
            {
                mod = num % 10;
                if (mod >= 5)
                {
                    mod = 9 - mod;
                    newMerge += to_string(mod);
                }
                else
                    newMerge += to_string(mod);
                num = num / 10;
            }
            reverse(newMerge.begin(), newMerge.end());
            strIndexZero = newMerge[0];
            if (strIndexZero.compare(strZero) == 0)
                newMerge.replace(0, 1, strNine);
            std::cout << newMerge;
        }
        return 0;
    }
