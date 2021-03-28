
def merge(a,b):
    i=0
    j=0
    t=[]
    while(i<len(a) and j<len(b)):
        if(a[i]<b[j]):
            t.append(a[i])
            i+=1
        else:
            t.append(b[j])
            j+=1
    while(i<len(a)):
        t.append(a[i])
        i+=1
    while(j<len(b)):
        t.append(b[j])
        j+=1
    # print('t',t)
    return t

def mergeSort(a):
    if(len(a)==1):
        return a
    mid = len(a)//2
    x=mergeSort(a[:mid])
    # print('x',x)
    y=mergeSort(a[mid:])
    # print('y',y)

    return merge(x,y)

print(mergeSort([13,2,6,7,8,1,3,2]))