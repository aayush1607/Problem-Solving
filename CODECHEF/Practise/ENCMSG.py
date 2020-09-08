# cook your dish here
'''
shizxvzsg
sxuv
'''
t=int(input())
for i in range(t):
    l=int(input())
    s=list(input())
    
    if(l%2!=0):
        l-=1
    for j in range(0,l,2):
        temp=s[j+1]
        s[j+1]=s[j]
        s[j]=temp
    
    for j in range(len(s)):
        if(s[j]=='a'):
            s[j]='z'
    
        elif(s[j]=='b'):
            s[j]='y'
            
        elif(s[j]=='c'):
            s[j]='x'
        elif(s[j]=='d'):
            s[j]='w'
        elif(s[j]=='e'):
            s[j]='v'
        elif(s[j]=='f'):
            s[j]='u'
        elif(s[j]=='g'):
            s[j]='t'
        elif(s[j]=='h'):
            s[j]='s'
            
        elif(s[j]=='i'):
            s[j]='r'
        elif(s[j]=='j'):
            s[j]='q'
        elif(s[j]=='k'):
            s[j]='p'
        elif(s[j]=='l'):
            s[j]='o'
        elif(s[j]=='m'):
            s[j]='n'
        elif(s[j]=='n'):
            s[j]='m'
        elif(s[j]=='o'):
            s[j]='l'
        elif(s[j]=='p'):
            s[j]='k'
        elif(s[j]=='q'):
            s[j]='j'
        elif(s[j]=='r'):
            s[j]='i'
        elif(s[j]=='s'):
            s[j]='h'
        elif(s[j]=='t'):
            s[j]='g'
        elif(s[j]=='u'):
            s[j]='f'
        elif(s[j]=='v'):
            s[j]='e'
        elif(s[j]=='w'):
            s[j]='d'
        elif(s[j]=='x'):
            s[j]='c'
        elif(s[j]=='y'):
            s[j]='b'
        else:
            s[j]='a'
    
    listToStr = ''.join(map(str, s)) 
    print(listToStr)  
