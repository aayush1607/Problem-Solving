# cook your dish here
try:
    t=int(input())
    for i in range(t):
        n,m,k=map(int,input().split())
        if(m==0):
            print(k)
        else:
            x=k//(n+m)
            print((n*x)+min(k%(m+n), n))
except:
    pass
