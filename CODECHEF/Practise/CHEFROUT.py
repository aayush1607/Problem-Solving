# cook your dish here
try:
    t=int(input())
    for i in range(t):
        d={'C':1,'E':2,'S':3}
        s=input()
        m=d[s[0]]
        f=0
        for i in range(1,len(s)):
            if(m>d[s[i]]):
                print('no')
                f=1
                break
            m=d[s[i]]
        if(f==0):
            print('yes')
except:
    pass
        

        
