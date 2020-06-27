#include <iostream>
#include<bits/stdc++.h>
#define max 10
using namespace std;

void sieve()
{
	
	int arr[max], i, j;
	for (i = 0; i < max; i++)
	{

		arr[i] = 1;
	}

	arr[0] = 0;
	arr[1] = 0;

	for (i = 2; i < max; i++)
	{

		if (i * i < max)
		{

			for (j = i * i; j < max; j += i)
			{


				arr[j] = 0;
			}
		}
	}


	for (i = 1; i < max; i++)
	{
	      if(arr[i]==1)
                  cout << i<< "\n";
	}
}



int main()
{
	// your code goes here


	sieve();

	return 0;
}

