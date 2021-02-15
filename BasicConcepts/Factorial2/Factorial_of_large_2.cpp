
#include <bits/stdc++.h>
using namespace std;
#define MAX 100

string factorial(long long n)
{

    if(n>MAX)
    {
        cout<<"OverFlow";
        return "";
    }
    long long i;
    long double sum=0;

    if(n==0){
        return"1";
    }

    for(i=1;i<=n;i++)
    {
        sum+=log(i);
    }

    string result= to_string(round(exp(sum)));
    return result;

}

int main()
{
    cout<<factorial(100)<<"\n";
}