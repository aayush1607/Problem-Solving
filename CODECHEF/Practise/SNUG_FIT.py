# cook your dish here
try:
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a.sort()
        b.sort()
        s=0
        for i in range(n):
            s=s+min(a[i],b[i])
        print(s)
except:
    pass
