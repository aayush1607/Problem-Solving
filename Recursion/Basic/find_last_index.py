def find_last(a,si,x):
    l=len(a)
    if(l==si):
        return -1
    idx=find_last(a,si+1,x)
    if(idx==-1):
        if(a[si]==x):
            return si
        return -1
    return idx

print(find_last([2,3,1,3,4],0,1))