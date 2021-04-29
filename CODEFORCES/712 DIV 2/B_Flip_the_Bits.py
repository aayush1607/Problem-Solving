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
        a1=list(input())
        a2=list(input())
        a1=list(map(int,a1))
        a2=list(map(int,a2))
        d=Counter(a1)
        d2=Counter(a2)
        if(a1==a2):
            print('YES')
        else:
            # print(a1,a2)
            zeros=Counter()
            ones=Counter()
            if(a1[0]==0):
                zeros[0]=1
            if(a1[0]==1):
                ones[0]=1
            for i in range(1,n):
                if(a1[i]==0):
                    zeros[i]=zeros[i-1]+1
                    ones[i]=ones[i-1]
                else:
                    zeros[i]=zeros[i-1]
                    ones[i]=ones[i-1]+1
            # print(zeros,ones)
            flag=0
            f=0
            for i in range(n-1,-1,-1):
                if(flag==0):
                    x=a1[i]
                if(flag==1):
                    x=flag-a1[i]
                if(zeros[i]==ones[i]):
                    if(x!=a2[i]):
                        if(flag==0):
                            flag=1
                        else:
                            flag=0
                else:
                    if(x!=a2[i]):
                        print("NO")
                        f=1
                        break
            if(f==0):
                print("YES")






            




                    

if __name__ == "__main__":
    main()