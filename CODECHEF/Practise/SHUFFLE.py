# cook your dish here
'''
Example Input
2
4 1
1 4 2 3
4 2
1 4 2 3
Example Output
yes
no
'''
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    a='yes'
    l2=l.copy()
    l2.sort()
    for j in range(k):
        q=[]
        q2=[]
        for p in range(j,len(l),k):
            q.append(l[p])
            q2.append(l2[p])
        q.sort()
        if(q!=q2):
            a='no'
    print(a)
        
            
        
    
