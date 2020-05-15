// { Driver Code Starts
//Initial Template for C++

#include<iostream>
using namespace std;


 // } Driver Code Ends


//User function Template for C++

// Function to count set bits in the given number x
// n: input to count the number of set bits
int countSetBits(int n){
    int i,j,c=0;
    // Your logic here
    for ( i = 1; i <=n; i++)
    {
        /* code */
        j=i;
        while(j>0){
            j=j&(j-1);
            c++;

        }
    }
    return c;
    
    
    
    
}

// { Driver Code Starts.

// Driver code
int main()
{
	 int t;
	 cin>>t;// input testcases
	 while(t--) //while testcases exist
	 {
	       int n;
	       cin>>n; //input n
	       
	       cout << countSetBits(n) << endl;// print the answer
	  }
	  return 0;
}  // } Driver Code Ends