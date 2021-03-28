def partition(a,s,e):

    first=a[s]
    c=0
    for i in range(s+1,e+1):
        if(a[i]<first):
            c+=1
    c+=s
    a[c],a[s]=a[s],a[c]
    i=s
    j=e
    while(i<c and j>c):
        if(a[i]>=a[c]):
            if(a[j]<a[c]):
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
            else:
                j-=1
        if(a[j]<a[c]):
            if(a[i]>=a[c]):
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
            else:
                i+=1
    return c

def quickSort(a,s,e):
    if(s>=e):
        return a
    
    i=partition(a,s,e)
    quickSort(a,s,i-1)
    quickSort(a,i+1,e)

a=[13,2,6,7,8,1,3,2]
quickSort(a,0,7)
print(a)