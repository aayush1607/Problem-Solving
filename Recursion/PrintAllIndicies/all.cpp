// Coded by __auc__
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

int allIndex(int a[], int size, int x, int out[] ) {

	if (size == 0) {
		return 0;
	}

	int outsize = allIndex(a + 1, size - 1, x, out);
	if (a[0] == x)
	{

		for (int i = outsize - 1; i >= 0 ; i--)
		{
			out[i + 1] = out[i] + 1;
		}
		out[0] = 0;

		return outsize + 1;

	}
	else
	{
		for (int i = 0; i < outsize ; ++i)
		{
			out[i] += 1;
		}
		return outsize;
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif


	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int t, x, y, i, j, k;
	input(t);
	while (t--)
	{	//code
		int x, n;
		cin >> n;
		int arr[n];
		int out[n];
		int a;
		fo(i, n)
		{
			cin >> arr[i];

		}
		cin >> x;

		a = allIndex(arr, n, x, out);
		fo(i, a)
		{
			cout << out[i] << " ";
		}
		cout << endl;


	}

	return 0;

}
