# cook your dish here
'''
Example Input
1
3 3
010
000
001
Example Output
1 0 1
2 1 1
1 1 0
'''
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l=[]
    for j in range(n):
        mat=list(input())
        for k in range(len(mat)):
            mat[k]=int(mat[k])
        l.append(mat)

    l1=[]
    
    q1=[]
    q2=[]
    for j in range(n):
        q1.append(sum(l[j]))
    for j in range(m):
        s=0
        for k in range(n):
            s+=l[k][j]
        q2.append(s)
    p=[]
    for j in range(n):
        p1=[]
        for k in range(m):
            p1.append([q1[j],q2[k]])
        p.append(p1)
    check1=0
    check2=0
    for j in q1:
        if(j!=0):
            check1=1
    for j in q2:
        if(j!=0):
            check2=1
    if(check1==0 and check2==0):
        for j in range(n):
            for k in range(m):
                print("-1",end=' ')
            print()
    else:
        for j in range(n):
            f=[]
            for k in range(m):
                if(p[j][k][0]>0 or p[j][k][1]>0):
                    if(l[j][k]==1):
                        f.append(0)
                    else:
                        f.append(1) 
                elif(p[j][k][0]==0 and p[j][k][1]==0):
                    f.append(2)
            l1.append(f)
                    
        for j in range(n):
            for k in range(m):
                print(l1[j][k],end=' ')
            print()
                
      
    
