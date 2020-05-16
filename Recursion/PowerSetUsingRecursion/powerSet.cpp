// { Driver Code Starts
//Initial Template for C++


// CPP program to generate power set
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends


//User function Template for C++

//Complete this function
void subset(string s,vector<string> &v,string curr,int i)
{
    if(s.length()==i)
    {
        v.push_back(curr);
        return;
    }
    
    
    subset(s,v,curr,i+1);
    subset(s,v,curr+s[i],i+1);
}
vector <string> powerSet(string s)
{
   //Your code here
   vector <string> v;
   subset(s,v,"",0);
   return v;
   
   
   
   
}


// { Driver Code Starts.


// Driver code
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        string s;
        cin>>s;
        vector<string> ans = powerSet(s);
        sort(ans.begin(),ans.end());
        for(auto x:ans)
        cout<<x<<" ";
        cout<<endl;
        
        
    }

return 0;
}   // } Driver Code Ends