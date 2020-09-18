#include <iostream>
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
#define endl '\n'
#define print(t) cout<<t<<"\n"
#define input(t) cin>>t
#define fo(i,n) for(i=0;i<n;i++)
#define Fo(i,k,n) for(i=k;k<n?i<n:i>n;k<n?i+=1:i-=1)
#define si(x) scanf("%d",&x)
#define pi(x) printf("%d\n",x)
#define ps(s) printf("%s\n",s)
#define deb(x) cout<<#x<<"="<<x<<endl
#define deb2(x,y) cout<<#x<<"="<<x<<","<<#y<<"="<<y<<endl
#define pb puch_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(),x.end()
#define clr(x) memset(x,0,sizeof(x))
#define sortall(x) sort(all(x))
#define tr(it,a) for(auto it=a.begin();it!=a.end();it++)



typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef map<int, int> mii;
typedef set<int> si;
typedef multiset<int> msi;
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int  uint64;
const int mod = 1000000007;
/*
for(int i=0;i<n;i++)
{

}
*/

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t, k;
    cin >> k;
    cin >> t;
    while (t--)
    {
        int n;

        cin >> n;


        int tempSum = 0;
        if (n % 2 == 0) {

            int sum = (n * (n + 1)) / 2;
            if (sum % 2 == 0) {
                cout << 0 << endl;
                for (int i = 2; i < n + 2 ; ++i)
                {

                    tempSum = (i * (i + 1)) / 2;
                    if (tempSum % 2 == 0) {
                        cout << 0;
                    }
                    else {
                        cout << 1;
                    }


                }
                cout << endl;
            }
            else {
                cout << 1 << endl;
                for (int i = 2; i < n + 2 ; ++i)
                {

                    tempSum = (i * (i + 1)) / 2;
                    if (tempSum % 2 == 0) {
                        cout << 0;
                    }
                    else {
                        cout << 1;
                    }


                }
                cout << endl;

            }



        }

        else {

            int sum = (n * (n + 1)) / 2;
            if (sum % 2 == 0) {
                cout << 0 << endl;
                for (int i = 1; i < n + 1 ; ++i)
                {

                    tempSum = (i * (i + 1)) / 2;
                    if (tempSum % 2 == 0) {
                        cout << 0;
                    }
                    else {
                        cout << 1;
                    }


                }
                cout << endl;
            }
            else {
                cout << 1 << endl;
                for (int i = 1; i < n + 1 ; ++i)
                {

                    tempSum = (i * (i + 1)) / 2;
                    if (tempSum % 2 == 0) {
                        cout << 0;
                    }
                    else {
                        cout << 1;
                    }


                }
                cout << endl;

            }



        }

    }

    return 0;

}
