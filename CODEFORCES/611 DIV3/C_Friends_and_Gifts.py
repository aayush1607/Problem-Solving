import os
import sys
from collections import Counter
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")




def main():
    n=int(input())
    g=list(map(int,input().split()))
    outgoing=Counter()
    for i in range(len(g)):
        g[i]-=1
        if(g[i]!=-1):
            outgoing[i]+=1
        
    incoming=Counter(g)
    incoming[-1]=0

    both_zero=[]
    for i in range(n):
        if(incoming[i]==0 and outgoing[i]==0):
            both_zero.append(i)
    if(len(both_zero)>1):
        x=0
        for i in range(len(both_zero)):
            g[both_zero[i]]=both_zero[(i+1)%(len(both_zero))]
            incoming[both_zero[(i+1)%(len(both_zero))]]+=1
            outgoing[both_zero[i]]+=1

    elif(len(both_zero)==1):
        x=0
        while(True):
            if(x!=both_zero[0] and incoming[x]==0):
                g[both_zero[0]]=x
                incoming[x]+=1
                outgoing[both_zero[0]]+=1
                break
            x+=1
    incomings=[]
    for i in range(n):
        if(incoming[i]==0):
            incomings.append(i)
    p=0
    for i in range(n):
        if(outgoing[i]==0):
            g[i]=incomings[p]
            p+=1
    for i in g:
        print(i+1,end=' ')





    


        

if __name__ == "__main__":
    main()