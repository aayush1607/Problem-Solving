import sys
import math

# zz=not __debug__
# if not zz:
#     sys.stdin=open('input.txt', 'r')
#     sys.stdout=open('output.txt','w')


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if(sorted(a)==a):
        print(0)
    else:
        ans=1
        c=0
        cc=0
        for i in range(n):
            if(a[i]!=i+1):
                c+=1
            if(a[i]==i+1):
                if(c>0):
                    cc+=1
                    if(cc>=2):
                        ans=2
                    c=0
                
        if(c>0):
            cc+=1
            if(cc>=2):
                ans=2
        
        print(ans)

