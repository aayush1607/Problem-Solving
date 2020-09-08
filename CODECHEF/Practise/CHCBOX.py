# cook your dish here
'''
Example Input
2
6
1 1 2 1 1 1
6
1 1 2 1 1 2
Example Output
3
0
'''

t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=max(l)
    l=l[::-1]

    for j in range(len(l)):
        if(l[j]==m):
            index=j
            break
    l=l[::-1]
    ind=l.index(m)
    ind=len(l)//2-ind-1
    print(max(0,index-ind))
