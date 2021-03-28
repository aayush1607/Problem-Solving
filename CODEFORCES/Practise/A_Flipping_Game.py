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
    t=1
    for _ in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        a=[]
        for i in l:
            if(i==0):
                a.append(1)
            else:
                a.append(-1)
        # print(a)
        max_ending_so_far=0
        max_ending_here=0
        idx1=0
        idx2=0    
        for i in range(n):
            max_ending_here+=a[i]
            if(max_ending_here<0):
                idx1=i
                print('idx1',idx1)
                max_ending_here=0
            if(max_ending_so_far<max_ending_here):
                idx2=i
                print('idx2',idx2)
                max_ending_so_far=max_ending_here


        
        # print(l[idx1].count(1)+c+l[idx2+1:].count(1))
                


if __name__ == "__main__":
    main()