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
    t=int(input())
    for _ in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        if(l[0]<0):
            f=0
        else:
            f=1
        k=1
        for i in range(1,len(l)):
            if(l[i]>0 and f==0):
                f=1
                k+=1
            elif(l[i]<0 and f==1):
                f=0
                k+=1
        # print(k)

        s=l[0]
        if(l[0]<0):
            f=0
        else:
            f=1
        prev=l[0]
        for i in range(1,len(l)):
            # print('s',s)
            if(k==0):
                break
            if(l[i]>0 and prev<0):
                s+=l[i]
                f=1
                k-=1
                prev=l[i]
            elif(l[i]<0 and prev>0):
                s+=l[i]
                f=0
                k-=1
                prev=l[i]
            elif(l[i]>0 and prev>0):
                if(s-prev+l[i]>s):
                    s=s-prev+l[i]
                    prev=l[i]
            elif(l[i]<0 and prev<0):
                if(s-prev+l[i]>s):
                    s=s-prev+l[i]
                    prev=l[i]
            

        print(s)


if __name__ == "__main__":
    main()