
import sys

import math



'''
https://www.codechef.com/SEPT20B/status/CHFNSWAP

Example Input
5
1
2
3
4
7
Example Output
0
0
2
2
3
'''
def roots( a, b, c):  

    dis = b * b - 4 * a * c  
    sqrt_val = math.floor(math.sqrt(abs(dis)))
       

    if(((-b + sqrt_val)//(2 * a))>=0):
        return ((-b + sqrt_val)//(2 * a))  
      
def main():
    t=int(input())
    

    
    for _ in range(t):
        n=int(input())
        sumt=(n*(n+1))//2
        if(sumt%2!=0):
            print(0)
        else:
            if(n==3):
                print(2)
            else:
                a=(roots(1,1,-sumt))
 
                a=n-a
                sum1=((n-a)*((n-a)+1))//2
                sum2=sumt-sum1
          
                if(sum2==sum1):
    
                    num=n-a
                    ans=((a*(a-1))//2)+(num*(num-1))//2+a
                    
                    print(ans)
                else:
                    print(a)


        
        
    


if __name__ == "__main__":
    main()