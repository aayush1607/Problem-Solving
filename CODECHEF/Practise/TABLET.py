# cook your dish here
t=int(input())
for i in range(t):
    n,b=map(int,input().split())
    a=0
    for j in range(n):
        h,w,p=map(int,input().split())
        if(p<=b):
            if(a<h*w):
                a=h*w
    if(a==0):
        print("no tablet")
    else:
        print(a)
            
        
