# cook your dish here
try:
    n=int(input())
    for i in range(n):
        a,b,c=(map(int,input().split()))
        if(a==0 or b==0 or c==0):
            print('NO')
        elif(a+b+c==180):
            print('YES')
        else:
            print('NO')

except:
    pass
