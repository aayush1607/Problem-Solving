import os
import sys
from collections import Counter
from io import BytesIO, IOBase
import math
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
    t=1
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))

        c=0
        d=Counter(a)
        x=min(d[3],d[1])
        c+=x
        d[3]-=x
        d[1]-=x

    
        c+=d[2]//2
        d[2]-=(2*(d[2]//2))


        x=min(d[2],d[1]//2)
        c+=x    
        d[1]-=(x*2)
        d[2]-=(x)

        x=d[1]//4
        c+=x
        d[1]-=(4*x)


        x=min(d[2],d[1])
        c+=x
        d[2]-=x
        d[1]-=x
        c+=math.ceil(d[1]/4)
        d[1]-=(d[1]//4)*4
        c+=math.ceil(d[2]/2)
        d[2]-=(d[2]//2)*2
        c+=d[3]
        c+=d[4]
        print(c)





if __name__ == "__main__":
    main()