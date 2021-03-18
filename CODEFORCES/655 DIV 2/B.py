import sys
import math

# zz=not __debug__
# if not zz:
#     sys.stdin=open('input.txt', 'r')
#     sys.stdout=open('output.txt','w')


def prime(n): 
	if (n == 1): 
		return False
	for i in range(2, n + 1): 
		if i * i > n: 
			break
		if (n % i == 0): 
			return False 
	return True






t=int(input())
for _ in range(t):
    n=int(input())
    if(prime(n)):
        print(1,n-1)
    else:
        for i in range(2,n+1):
            if(i*i>n):
                break
            if(n%i==0):
                print(n//i,n//i*(i-1))
                break
