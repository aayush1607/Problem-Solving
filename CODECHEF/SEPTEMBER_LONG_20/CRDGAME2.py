#!/usr/bin/env python

'''
CRDGAME2
https://www.codechef.com/SEPT20B/problems/CRDGAME2
'''
import os
import sys
from io import BytesIO, IOBase

def ncr(n, r, p):
    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den, p - 2, p)) % p

def main():
    mod=1000000007
    t=int(input())
    for _ in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        maxe=l[0]
        for i in range(1,len(l)):
            if(l[i]>maxe):
                maxe=l[i]
        freq=0
        for i in range(len(l)):
            if(l[i]==maxe):
                freq+=1
        combinations=pow(2,n,mod)
        if(freq%2!=0):
            print(combinations%mod)
        else:
            print((combinations%mod-((ncr(freq,freq//2,mod))%mod*(pow(2,n-freq,mod))%mod))%mod)
if __name__ == "__main__":
    main()


# region fastio

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

# endregion








 