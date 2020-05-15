// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends


//User function Template for C++

// Function to find number of bits to be flip
// to convert A to B
int countSetBits(int n)
{
    int c=0;
    while (n>0)
    {
        n=n&(n-1);
        c++;
    }
    return c;
    
}
int countBitsFlip(int a, int b){
    
    // Your logic here
    int x=a^b;
    return countSetBits(x);


    
}

// { Driver Code Starts.

// Driver Code
int main()
{
	int t;
	cin>>t;// input the testcases
	while(t--) //while testcases exist
	{
		int a,b;
		cin>>a>>b; //input a and b

		cout<<countBitsFlip(a, b)<<endl;
	}
	return 0;
}  // } Driver Code Ends