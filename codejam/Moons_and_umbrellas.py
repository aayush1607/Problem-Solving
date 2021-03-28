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


def cost(s,x,y):
    return (s.count('CJ')*x)+(y*s.count('JC'))

def main():
    t=int(input())
    for i in range(t):
        l=list(input().split())
        x=int(l[0])
        y=int(l[1])
        s=l[2]
        # print(x,y,s)
        ss=""
        for j in range(len(s)):
            if(s[j]=='?'):
                if(j==0):
                    ss+=s[j]
                elif(j==len(s)-1):
                    ss+=s[j]

            else:
                ss+=s[j]
        # print(ss,ss.count('CJ'),ss.count('JC'))

        if(ss[0]=='?' and ss[-1]=="?"):
            ss1='C'+ss[1:len(ss)-1]+'J'
            ss2='J'+ss[1:len(ss)-1]+'C'
            ss3='J'+ss[1:len(ss)-1]+'J'
            ss4='C'+ss[1:len(ss)-1]+'C'
            mincost = (min(cost(ss1,x,y),cost(ss2,x,y),cost(ss3,x,y),cost(ss4,x,y)))
        else:
            if(ss[0]=='?'):
                ss1='C'+ss[1:]
                ss2='J'+ss[1:]
                mincost = (min(cost(ss1,x,y),cost(ss2,x,y)))
            elif(ss[-1]=='?'):
                ss1=ss[:len(ss)-1]+'C'
                ss2=ss[:len(ss)-1]+'J'
                mincost = (min(cost(ss1,x,y),cost(ss2,x,y)))
            else:
                mincost = (cost(ss,x,y))
        print("Case #"+str(i+1)+": "+str(mincost))



if __name__ == "__main__":
    main()