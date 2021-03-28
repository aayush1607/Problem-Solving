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
    for tc in range(t):
        r,c=map(int,input().split())

        l=[]
        for i in range(r):
            column = list(map(int,input().split()))
            l.append(column)
        
        leftToRight = list(map(list, l))
        print("LR:",leftToRight)
        for i in range(len(leftToRight)):
            for j in range(1,len(leftToRight[i])):
                if(leftToRight[i][j]>0):
                    leftToRight[i][j]+=leftToRight[i][j-1]

        rightToLeft = list(map(list, l))
        for i in range(len(rightToLeft)):
            for j in range(len(rightToLeft[i])-2,-1,-1):
                if(leftToRight[i][j]>0):
                    leftToRight[i][j]+=leftToRight[i][j+1]

        toptoDown =  list(map(list, l))
        for i in range(1,len(toptoDown)):
            for j in range(len(toptoDown[i])):
                if(toptoDown[i][j]>0):
                    toptoDown[i][j]+=toptoDown[i-1][j]
                      
        downtoTop =  list(map(list, l))
        for i in range(len(downtoTop)-1):
            for j in range(len(downtoTop[i])):
                if(downtoTop[i][j]>0):
                    downtoTop[i][j]+=downtoTop[i+1][j]
        print(leftToRight)
        print(rightToLeft)
        print(toptoDown)
        print(downtoTop)

if __name__ == "__main__":
    main()