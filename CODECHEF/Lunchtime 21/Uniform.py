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


def merge(arr):
        #src--> https://www.geeksforgeeks.org/merging-intervals/
        arr.sort(key = lambda x: x[0])
        m = []
        s = -10000
        max = -100000
        for i in range(len(arr)):
            a = arr[i]
            if a[0] > max:
                if i != 0:
                    m.append([s,max])
                max = a[1]
                s = a[0]
            else:
                if a[1] >= max:
                    max = a[1]
 
        if max != -100000 and [s, max] not in m:
            m.append([s, max])
        
        return m
mod=998244353
def main():
    t=int(input())
    for _ in range(t):
        c,n,m=map(int,input().split())
        x=[]
        for i in range(c):
            p=int(input())
            l=list(map(int,input().split()))
            for j in range(0,len(l),2):
                left=l[j]
                right=l[j+1]
                x.append([left,right])
        merged=merge(x)
        
        # lc = [0]*n
        # for i in merged:
        #     for j in range(i[0],i[1]+1):
        #         lc[j-1] = 1
        lc = []
        for i in range(len(merged)):
            a = merged[i][0]
            b = merged[i][1]
            for j in range(a, b+1):
                lc.append(j)


        # cc = 0
        # for j in range(1, n+1):
        #     if j not in lc:
        #         cc = (cc+m)%mod     
        # print(merged)
        pre=[0]*(n+1)
        # print(pre)
        for j in range(len(merged)):
            pre[merged[j][0]-1]=1
            # print(merged[j][1])
            pre[merged[j][1]]=-1
        # print(pre)
        for j in range(1,len(pre)):
            pre[j]+=pre[j-1]
        # print(pre)
        cc=(((pre[:len(pre)-1].count(0))%mod)*(m%mod))%mod
        cc=(cc+(len(merged)*m)%mod)%mod
    
        print(cc)


if __name__ == "__main__":
    main()