// Coded by __auc__
/*
SEPT LONG CODECHEF
https://www.codechef.com/SEPT20B/problems/ADAMAT
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

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif


	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int t, x, y, i, j, k;
	cin >> t;
	while (t--)
	{	//code

		int n, i, j;
		cin >> n;
		int arr[n][n], s[n - 1] = {};
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> arr[i][j];

			}
		}

		for (int i = 1; i < n; i++) {
			if (arr[0][i] == i + 1) {

				s[i - 1] = 0;

			}
			else {
				s[i - 1] = 1;
			}
		}
		int s2[n - 1];
		for (int i = 0; i < n - 1; ++i)
		{
			s2[i] = s[i];
			/* code */
		}
		int lastone = -1;
		int lastzero = -1;
		for (int i = n - 2; i >= 0; --i)
		{
			if (s[i] == 1) {
				lastone = i;
				break;

			}
		}
		for (int i = n - 2; i >= 0; --i)
		{
			if (s[i] == 0) {
				lastzero = i;
				break;

			}
		}
		if (lastone == -1) {
			cout << 0 << endl;

		}
		else if (lastzero == -1) {
			cout << 1 << endl;


		}

		else {

			int cnt = 0;
			while (accumulate(s, s + (n - 1), 0) > 0) {


				cnt++;

				for (int i = lastone; i > -1; i--)
				{
					if (s[i] == 0) {
						s[i] = 1;
					}

					else if (s[i] == 1) {
						s[i] = 0;
					}

				}

				int lsttemp = -1;
				for (int i = lastone - 1; i >= 0; i--)
				{
					if (s[i] == 1) {
						lsttemp = i;
						break;
					}
				}


				lastone = lsttemp;
				if (lastone == -1) {

					break;

				}

			}
			int cnt2 = 0;
			while (accumulate(s2, s2 + (n - 1), 0) != n - 1) {


				cnt2++;


				for (int i = lastzero; i > -1; i--)
				{
					if (s2[i] == 0) {
						s2[i] = 1;
					}

					else if (s2[i] == 1) {
						s2[i] = 0;
					}

				}

				int lsttemp = -1;
				for (int i = lastzero; i >= 0; i--)
				{
					if (s2[i] == 0) {
						lsttemp = i;
						break;
					}
				}


				lastzero = lsttemp;

				if (lastzero == -1) {


					break;

				}

			}



			cout << min(cnt, cnt2 + 1) << endl;


		}







	}

	return 0;

}
