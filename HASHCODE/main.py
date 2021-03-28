import sys
from collections import Counter






def solve(duration,intersections,streets,cars,bonus,all_streets,all_cars):
    all_intersections=Counter()
    #print(all_streets)
    for street in all_streets:
        #print(all_streets[street])
        if(all_intersections[all_streets[street][1]]==0):
            all_intersections[all_streets[street][1]]=[]
        all_intersections[all_streets[street][1]].append((street,all_streets[street][0],all_streets[street][2]))
    #print(all_intersections)
    
    
    count_streets=Counter()
    
    for i in all_cars:
        for j in range(len(all_cars[i])):
            count_streets[all_cars[i][j]]+=1
    #print(count_streets)

    print(len(all_intersections))    
    for i in all_intersections:
        l=[]
        #print(i)
        #print(len(all_intersections[i]))
        mmax=0
        avg=0
        maxstreet=""
        for j in range(len(all_intersections[i])):
            avg+=count_streets[all_intersections[i][j][0]]
        avg=avg//len(all_intersections[i])
        mmax=avg
        ss=[]
        for j in range(len(all_intersections[i])):
            ss.append([count_streets[all_intersections[i][j][0]],all_intersections[i][j][0]])
        ss.sort()
        pp=1

        for j in range(len(ss)):
            l.append((i,ss[j][1],j+1))
        # for j in range(len(all_intersections[i])):
        #     if(all_intersections[i][j][0]==maxstreet):
        #         l.append((i,all_intersections[i][j][0],7))
        #     else:
        #         l.append((i,all_intersections[i][j][0],2))
        

                
        print(l[0][0])
        print(len(l))
        
        for i in l:
            print(i[1],i[2])
        

    


    

        




def read():
    duration,intersections,streets,cars,bonus=map(int,input().split())
    all_streets=Counter()
    for i in range(streets):
        b,e,name,l=input().split()
        b=int(b)
        e=int(e)
        l=int(l)
        all_streets[name]=[b,e,l]
    all_cars= Counter()
    for i in range(cars):
        temp=(input().split())
        p=temp[0]
        paths=temp[1:]
        all_cars[i+1]=paths
    solve(duration,intersections,streets,cars,bonus,all_streets,all_cars)






    






def main():

    input_dir="./input/"
    output_dir="./output/"
    input_files=["a","b","c","d","e","f"]
    for i in range(len(input_files)):

        input_path = input_dir+input_files[i]+".txt"
        output_path = output_dir+input_files[i]+".out"

        sys.stdin=open(input_path, 'r')
        sys.stdout=open(output_path,'w')


        read()
        
        


if __name__ == "__main__":
    main()