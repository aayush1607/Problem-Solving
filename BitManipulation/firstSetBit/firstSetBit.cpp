// { Driver Code Starts
//Initial Template for C++

#include<iostream>
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends


//User function Template for C++

/*  function to find position of first set 
    bit in the given number
 * n: given input for which we want to get
      the position of first set bit
 */
unsigned int getFirstSetBit(int n){
    
    if(n==0)
    return 0;
    else
    {
        int k=1,c=1;
     
        while((n&k)==0)
        {
            k=k<<1;
           
            c++;
        }
        return c;
    }
    
    // Your code here
    
    
}

// { Driver Code Starts.

// Driver code
int main()
{
    int t;
    cin>>t; // testcases
    while(t--)
    {
        int n;
        cin>>n; //input n
        
        printf("%u\n", getFirstSetBit(n)); // function to get answer
    }
	return 0;
}
  // } Driver Code Ends