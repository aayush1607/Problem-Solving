import os
import sys
from collections import Counter
from io import BytesIO, IOBase
from itertools import permutations
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


def cost(n,l):
    c=0
    minn=max(l)+1
    for j in range(n-1):
        minnum=minn
        minidx=j
        for jj in range(j,n):
            if(l[jj]<minnum):
                minnum=l[jj]
                minidx=jj
        x=l[j:minidx+1]
        x=x[::-1]
        l=l[:j]+x+l[minidx+1:]
        # print('l',l)
        c+=len(x)    
    return c

def main():
    t=int(input())
    for i in range(t):
        n,c=map(int,input().split())
        l=[]
        for j in range(1,n+1):
            l.append(j)
        if(c>(n*(n+1)//2)-1 or  c<n-1):
            print("Case #"+str(i+1)+": "+"IMPOSSIBLE")
        else:
            


        # f=0
        # # print(l)
        # for a in l:
        #     if(cost(len(a),a)==c):
        #         f=1
        #         print("Case #"+str(i+1)+": ",end="")
        #         for j in a:
        #             print(j,end=" ")
        #         print()
                         
            

        # if(f==0):
        #     print("Case #"+str(i+1)+": "+"IMPOSSIBLE")
            

if __name__ == "__main__":
    main()