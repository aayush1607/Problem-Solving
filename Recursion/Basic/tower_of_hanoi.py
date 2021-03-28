
def moves(n,src,helper,dest):
    if(n==1):
        print("move 1st disk from "+src+" to "+dest)
        return
    moves(n-1,src,dest,helper)
    print("move "+str(n)+"th disk from "+src+" to "+dest)
    moves(n-1,helper,src,dest)

moves(2,'A','B','C')
    