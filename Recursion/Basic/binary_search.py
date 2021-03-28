
def binary_search(a,l,h,x):
    mid = l-(l-h)//2
    if(a[mid]==x):
        return mid
    if(x<a[mid]):
        return binary_search(a,l,mid-1,x)
    return binary_search(a,mid+1,h,x)


print(binary_search([1,2,3,4,5],0,4,5))