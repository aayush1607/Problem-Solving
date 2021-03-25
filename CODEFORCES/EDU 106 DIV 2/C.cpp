#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ll t;
    cin >> t;
    while(t--)  {
        string s;
        cin >> s;
        ll flag = 1, n = s.length();
        
        for(int i = 1; i < n; i++)  {
            if(s[i-1] > s[i])   {
                flag = 0;
            }
        }
        if(flag == 1)   {
            cout << "YES" << "\n";
        }
        else    {
            flag = 0;
            for(int i = -1; i <= n; i++)    {
                ll last, flag1 = 1, flag2 = 1;
                if(i == -1) {
                    last = -1;
                    for(int j = 0; j < n; j++)  {
                        if(s[j] == '0') {
                            if(last != -1 && last + 1 == j)   {
                                flag1 = 0;
                                break;
                            }
                            last = j;
                        }
                    }
                    if(flag1 == 1)  {
                        //cout << "*"  << i << "\n";
                        flag = 1;
                        break;
                    }
                }
                else if(i == n) {
                    last = -1;
                    for(int j = 0; j < n; j++)  {
                        if(s[j] == '1') {
                            if(last != -1 && last + 1 == j)   {
                                flag1 = 0;
                                break;
                            }
                            last = j;
                        }
                    }
                    if(flag1 == 1)  {
                        //cout << "**"  << i << "\n";
                        flag = 1;
                        break;
                    }
                }
                else    {
                    last = -1;
                    for(int j = 0; j <= i; j++)  {
                        if(s[j] == '1') {
                            if(last != -1 && last + 1 == j)   {
                                flag1 = 0;
                                break;
                            }
                            last = j;
                        }
                    }
                    for(int j = i+1; j < n; j++)  {
                        if(s[j] == '0') {
                            if(last + 1 == j)   {
                                flag2 = 0;
                                break;
                            }
                            last = j;
                        }
                    }
                    if(flag1 == 1 && flag2 == 1)    {
                        flag = 1;
                        //cout << "***"  << i << "\n";
                        break;
                    }
                    
                }
            }
            
            
            if(flag == 1)    {
                cout << "YES" << "\n";
                continue;
            }
            
            else    {
                cout << "NO" << "\n";
            }
            
            
        }
    }
}