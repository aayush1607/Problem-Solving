'''input
4
5 2 5 3 1
3 0 0 0 0
4 4 1 4 0
2 1 1 1 1


'''

from bisect import bisect_right as bl
import random
RI = lambda : [int(_x) for _x in input().split()]
import sys
sys.stdout=open('output.txt','w')


def check(a,b,c,d1,u,r,l,d,n):
	if u == 0:
		if a==1 or b==1:
			return False
	if d == 0:
		if c==1 or d1==1:
			return False
	if l == 0:
		if a==1 or d1==1:
			return False
	if r == 0:
		if c==1 or b==1:
			return False
	

	if u == n:
		if a==0 or b==0:
			return False
	if d == n:
		if c==0 or d1==0:
			return False
	if l == n:
		if a==0 or d1==0:
			return False
	if r == n:
		if c==0 or b==0:
			return False


	if u == n-1:
		if a==0 and b==0:
			return False
	if d == n-1:
		if c==0 and d1==0:
			return False
	if l == n-1:
		if a==0 and d1==0:
			return False
	if r == n-1:
		if c==0 and b==0:
			return False

	if u == 1:
		if a==1 and b==1:
			return False
	if d == 1:
		if c==1 and d1==1:
			return False
	if l == 1:
		if a==1 and d1==1:
			return False
	if r == 1:
		if c==1 and b==1:
			return False
	return True

def ss(n,u,r,d,l):
    a=[list(map(int,list(bin(x)[2:]))) for x in range(16)]
    for x in range(len(a)):
        while (len(a[x])<4):
            a[x].insert(0,0)
    temp=[u,r,d,l]
    ans=False
    for x in range(len(a)):
        done=True
        for y in range(len(a[x])):
            cur=a[x][y]+a[x][(y+1)%4]
            left=temp[y]-cur
            if left>n-2 or left<0:
                done=False
        if done:
            ans=True
    if(ans):
        return "YES"
    else:
        return "NO"


ii=0
while(ii<100):
    n=random.randint(2,100)
    u=random.randint(0,1)
    r=random.randint(0,n)
    d=random.randint(0,1)
    l=random.randint(0,n)
    # n,u,r,d,l=5,2,5,3,1
    #a1=ss(n,u,r,d,l)
    ans="NO"
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d1 in range(2):
                    if( check(a,b,c,d1,u,r,l,d,n)):
                        ans="YES"

    if(ans=="NO"):
        ii+=1
        print(n,u,r,d,l)
        print(ans)
    # if(a1!=ans):
    #     print(a1,ans)
    #     print(n,u,r,d,l)


    