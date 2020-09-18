// Coded by __auc__


/*
https://www.codechef.com/SEPT20B/problems/COVID19B
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
	while (t--)
	{	//code
		int n;
		cin >> n;
		int arr[n][2];
		for (int i = 0; i < n; ++i)
		{
			int x;
			cin >> x;
			arr[i][0] = x;
			arr[i][1] = 0;
		}
		int minAns = n, maxAns = 1;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				arr[j][1] = 0;
			}

			arr[i][1] = 1;
			int left_max = arr[i][0];
			int left_index = i;
			for (int j = 0; j <= i ; ++j)
			{
				if (arr[j][0] > left_max) {
					left_max = arr[j][0];
					left_index = j;
				}
			}

			arr[left_index][1] = 1;
			for (int j = i; i < n; ++j)
			{
				if (arr[j][0] < left_max) {
					arr[j][1] = 1;
					for (int k = j ; k >= 0; k--)
					{
						if (arr[k][0] > arr[j][0]) {
							arr[k][1] = 1;
						}
					}
				}
			}
			int cnt = 0;

			for (int j = 0; j < n ; ++j)
			{
				if (arr[j][1] == 1) {
					cnt++;
				}
			}
			if (minAns > cnt) {
				minAns = cnt;
			}
			if (maxAns < cnt) {
				maxAns = cnt;
			}


		}
		cout << minAns << " " << maxAns << endl;



	}

	return 0;

}
