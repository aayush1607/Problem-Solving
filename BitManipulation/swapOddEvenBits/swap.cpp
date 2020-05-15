// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends


//User function Template for C++

// function to swap odd and even bits
unsigned int swapBits(unsigned int n)
{
	
	// Your code here
	int evenbits=n&0xAAAAAAAA;
	int oddbits=n&0x55555555;
	evenbits=evenbits>>1;
	oddbits=oddbits<<1;
	return(evenbits|oddbits);
	
}

// { Driver Code Starts.

// Driver code
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		unsigned int n;
		cin>>n;
		cout << swapBits(n) << endl;
	}
	return 0;
}  // } Driver Code Ends