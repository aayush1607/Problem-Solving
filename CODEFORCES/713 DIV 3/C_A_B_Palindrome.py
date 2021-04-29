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
    for i in range(t):
        a,b=map(int,input().split())
        s=list(input())
        n=a+b
        aa=0
        bb=0
        f=0
        for i in range(int(n/2)):
            if(s[i]!=s[n-i-1]):
                if(s[i]!='?' and s[n-i-1]!='?'):
                    print(-1)
                    f=1
                    break
                else:
                    if(s[i]=='?' and s[n-i-1]=='?'):
                        pass
                    else:
                        if(s[i]=='?'):
                            s[i]=s[n-i-1]
                        else:
                            s[n-i-1]=s[i]
        aa=s.count('0')
        bb=s.count('1')
        if(f==0):
            for i in range(int(n/2)):
                if(s[i]=='?'):
                    if(aa+2<=a):
                        s[i]='0'
                        s[n-i-1]='0'
                        aa+=2
                    else:
                        s[i]='1'
                        s[n-i-1]='1'
                        bb+=2
            # print(s)
            if(n%2!=0 and s[n//2]=='?'):

                if(aa+1<=a):
                    aa+=1
                    s[n//2]='0'
                else:
                    bb+=1
                    s[n//2]='1'
            if(s!=s[::-1] or s.count('0')!=a or s.count('1')!=b):
                print(-1)
            else:
                print("".join(s))


if __name__ == "__main__":
    main()