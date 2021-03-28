
def isSorted(a,si):
    l=len(a)
    if(si>=l-1):
        return True
    if(a[si]>a[si+1]):
        return False
    return isSorted(a,si+1)

print(isSorted([1,2,3,4],0))