# cook your dish here
'''
Sample Input:
2
1
3
Sample Output:
1
7
'''
t=int(input())
for i in range(t):
    n=int(input())
    print(pow(2,n,1000000007)-1)
