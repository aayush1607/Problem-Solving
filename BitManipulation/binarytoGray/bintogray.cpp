// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends


//User function Template for C++

// function to conver given N Gray to Binary
int grayToBinary(int n)
{
    
    // Your code here



    int num = n;

    while (n>=1){
        n=n>>1;
        num = (num^n);

    }
    return num;

    
}

// { Driver Code Starts.

// Driver code
int main()
{
    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
       cout<< grayToBinary(n)<<endl;
    }
}
  // } Driver Code Ends