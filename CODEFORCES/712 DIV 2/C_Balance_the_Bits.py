import os
import sys
from collections import Counter
from io import BytesIO, IOBase
# sys.setrecursionlimit(100000000)
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


def isB(exp):
    flag = True
    count = 0
    for i in range(len(exp)):
        if (exp[i] == '('):
            count += 1
        else:
            count -= 1
  
        if (count < 0):
  
            flag = False
            break
    if (count != 0):
        flag = False
  
    return flag

def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        s=input()
        d=Counter(list(s))
        x=''
        y=''
        cx=0
        cy=0
        if((d['0']%2==0 and d['1']%2==0) and (s[0]=='1' and s[-1]=='1')):
            k=0
            for j in range(n):
                if(s[j]=='1'):
                    if(k>d['1']//2-1):
                        x+=')'
                        y+=')'
                        cx-=1
                        cy-=1
                    else:
                        x+='('
                        y+='('
                        cx+=1
                        cy+=1
                    k+=1
                else:
                    if(cx>cy):
                        x+=')'
                        y+='('
                        cx-=1
                        cy+=1
                    else:
                        x+='('
                        y+=')'
                        cx+=1
                        cy-=1
                
            print("YES")    
            print(x)
            print(y)
        else:
            print("NO")




if __name__ == "__main__":
    main()