#include<iostream>
using namespace std;
#define MAX 200

//multiply fxn

int multiply(int x,int res[],int size){

    int carry=0;

    for(int i=0;i<size;i++)
    {
        int prod=res[i]*x+carry;
        res[i]=prod%10;  //last digit is ans

        carry=prod/10; //rest is carry

    }

    //put carry in res 
    while(carry)
    {
        res[size]=carry%10;
        carry=carry/10;
        size++;
    }
    return size;
}

void factorial(int n)
{

    int res[MAX];
    res[0]=1;
    int size=1;

    for (int x=2;x<n;x++)
    {

        size=multiply(x,res,size);
    }
    
    //print
    for (int i = size-1; i>=0; i--)
    {
        /* code */
        cout<<res[i];
    }
    cout<<endl;
    

}

int main()
{

    factorial(100);
}