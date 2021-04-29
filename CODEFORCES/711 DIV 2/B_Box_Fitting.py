import os
import sys
from collections import Counter
from io import BytesIO, IOBase
import math as m

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
    t=int(input())
    for _ in range(t):
        n,w=map(int,input().split())
        l=list(map(int,input().split()))
        W=Counter()
        for i in l:
            W[m.log2(i)]+=1
        
        ll=[]
        s=0
        x=0
        c=1
        p=[]
        for i in range(len(l)-1,-1,-1):
            if(s+l[i]<=w):
                s+=l[i]
                p.append(l[i])
                x=1
            else:
                ll.append(l[i])

        if(x==0):
            print(0)
        else:
            if(len(ll)==0):
                print(1)
            else:
                k=0
                for i in range(len(ll)):
                    if(ll[i]==p[k]):
                        k=(k+1)%len(p)
                    else:
                        c+=1
                print(c)

            

if __name__ == "__main__":
    main()