// { Driver Code Starts
//Initial Template for C++


#include <iostream>
using namespace std;


 // } Driver Code Ends


//User function Template for C++

//Complete this function
int countDigitsSum(int n)
{
    if(n<10)
    return n;
    
    return(n%10+countDigitsSum(n/10));
}
int digitalRoot(int n)
{
    //Your code here
    if(n<10)
    return n;
    
    return(digitalRoot(countDigitsSum(n)));
    
    
}

// { Driver Code Starts.


int main() {
	int T;
	cin>>T;
	while(T--)
	{
	    int n;
	    cin>>n;
	    
	    cout<<digitalRoot(n)<<endl;
	    
	    
	}
	return 0;
}  // } Driver Code Ends