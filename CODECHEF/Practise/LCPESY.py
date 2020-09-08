# cook your dish here
t=int(input())
for i in range(t):
    s1=list(input())
    s2=list(input())
    a=set(s1)
    b=set(s2)
    i=list(a.intersection(b))
    c=0
    for j in i:
        c+=min(s1.count(j),s2.count(j))
    print(c)
    
    
