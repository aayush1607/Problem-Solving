# def find_first(a,x):
#     l=len(a)
#     if(l==0):
#         return -1
#     if(a[0]==x):
#         return 0
#     return find_first(a[1:],x)+1
def find_first(a,si,x):
    l=len(a)
    if(l==si):
        return -1
    if(a[si]==x):
        return si
    return find_first(a,si+1,x)
print(find_first([2,3,1,4,1],0,1))