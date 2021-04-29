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

def countElements(a, n):
    cnt = [0] * (n + 1)
    ans = 0
    for k in a:
        cnt[k] += 1
 
    for l in range(n):
        sum = 0
        for r in range(l, n):
            sum += a[r]
            if (l == r):
                continue
            if (sum <= n):
                ans += cnt[sum]
                cnt[sum] = 0
    return ans


def main():
    t=int(input())
    for i in range(t):
        n,l,r,s=map(int,input.split())
        p=[]
        for i in range(1,n+1):
            p.append(i)
        s=0
        for i in range(l-1,r):
            s+=p[i]
        possible_change_plus=[]
        possible_change_minus=[]
        for i in range(l-1,r):
            x=p[i]
            for j in range(l-1):
                possible_change_minus.append(p[j]-x)
            for j in range(r,len(p)):
                possible_change_plus.append(p[j]-x)
        
        

        



if __name__ == "__main__":
    main()