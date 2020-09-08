# cook your dish here
'''
Sample Input:
3
3
5
4 1 2
5
2
4 4 3 2 2
5
1
4 2 3 1 1

Sample Output:
Impossible
Possible
Impossible
'''
def check(w):
    for j in range(len(w)):
        for k in range(len(w[j])):
            if(j+1>=w[j][k]):
                return("Impossible")
    return("Possible")
t=int(input())
for i in range(t):
    n=int(input())
    d=int(input())
    l=list(map(int,input().split()))
    l.sort()
    w=[]
    j=0
    while(j<len(l)):
        l2=[]
        for k in range(d):
            if(j<len(l)):
                l2.append(l[j])
            j+=1
        w.append(l2)
    
    print(check(w))
