// { Driver Code Starts
//Initial Template for C++

#include <iostream>
using namespace std;


 // } Driver Code Ends


//User function Template for C++

/*  Function to calculate the largest consecutive ones
*   x: given input to calculate the largest consecutive ones
*/
int maxConsecutiveOnes(int x)
{
    int c=0;
    // Your code here
    while(x>0){
        x=x&(x<<1);
        c++;
    }
    return c;
    
    
}



// { Driver Code Starts.

// Driver Code
int main() {
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		cout<<maxConsecutiveOnes(n)<<endl;
	}
	return 0;
}  // } Driver Code Ends