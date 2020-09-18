// Coded by __auc__

// FINXOR

/*
https://www.codechef.com/SEPT20B/problems/FINXOR
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>
#include <string>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <cstdio>
#include <cmath>

using namespace std;
using ll = long long;
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

/*
Example Input
4
3
1 2 3
3
3 2 1
3
0 0 0
3
1 3 2
Example Output
1 1
3 3
1 1
1 2

*/

bool isKthBitSet(int n, int k)
{
    if (n & (1 << (k - 1)))
        return true;
    else
        return false;
}
void decToBinary(int n)
{
    // array to store binary number
    int binaryNum[32];

    // counter for binary array
    int i = 0;
    while (n > 0) {

        // storing remainder in binary array
        binaryNum[i] = n % 2;
        n = n / 2;
        i++;
    }

    // printing binary array in reverse order
    for (int j = i - 1; j >= 0; j--)
        cout << binaryNum[j];
}
int main() {

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif


    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t;
    cin >> t;
    int res;
    for (int i = 0; i < t; ++i)
    {

        int n;
        cin >> n;
        int num = (int)(pow(2, 20) + 0.5);
        int ans = 0;
        int s;
        cout << 1 << " " << num << endl;
        fflush(stdout);
        cin >> s;
        s = s - (n * (num));
        if (s & (1)) {
            ans = ans | (1);
        }


        for (int i = 1; i < 20; ++i)
        {
            num = (int)(pow(2, i) + 0.5);
            int sx, kx;
            cout << 1 << " " << num << endl;
            fflush(stdout);
            cin >> sx;
            kx = (s - sx + (num) * n) / (2 * num);
            if (kx % 2 != 0) {
                ans = ans | (1 << i);
            }

        }
        cout << 2 << " " << ans << endl;
        fflush(stdout);
        cin >> res;
        if (res == -1) {
            break;
        }

    }

    return 0;

}
