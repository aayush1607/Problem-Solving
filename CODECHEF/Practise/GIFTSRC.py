# cook your dish here
'''
Example Input
3
5
LLLUR
7
LLLRUUD
8
LRULLUDU
Example Output
0 1
-1 1
-2 2
'''
t=int(input())
lr=["L","R"]
ud=["U","D"]
for i in range(t):
    l=0
    u=0
    n=int(input())
    x=0
    y=0
    s=input()
    for j in range(len(s)):
        if(l==0 and u==0):
            if(s[j]=="L"):
                x-=1
            if(s[j]=="R"):
                x+=1
            if(s[j]=="U"):
                y+=1
            if(s[j]=="D"):
                y-=1
        if(l==1 and u==0):
            if(s[j] not in lr):
                if(s[j]=="U"):
                    y+=1
                else:
                    y-=1
        if(l==0 and u==1):
            if(s[j] not in ud):
                if(s[j]=="L"):
                    x-=1
                else:
                    x+=1
        if(s[j] in lr):
            l=1
            u=0
        elif(s[j] in ud):
            l=0
            u=1
    print(x,y)
        
            
        
        
    
