

def main():
    
    
    for _ in range(1):
        
        a,b,k=map(int,input().split())
        if(k>=a+b-2):
            print("No")
        else:

            s=list(('1'*b+'0'*a))
            x=s.copy()
            #print((s))
            pos1=0
            for i in range(len(s)):
                if(s[i]=='1'):
                    pos1=i
                if(s[i]=='0'):
                    break
            #print(pos1)
            curr=pos1
            while(k):
                if(curr<len(s)-1):
                    s[curr],s[curr+1]=s[curr+1],s[curr]
                    curr+=1
                    k-=1
                else:
                    curr=pos1-1
            print("Yes")        
            print("".join(x))
            print("".join(s))




if __name__ == "__main__":
    main()