import os
import sys
from collections import Counter
from io import BytesIO, IOBase
import math

BUFSIZE = 8192

if sys.version_info[0]<3:
    from __built__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

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

def print(*args,**kwargs):
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()

if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# # For getting input from input.txt file 
# sys.stdin = open('input.txt', 'r')  
  
# # Printing the Output to output.txt file 
# sys.stdout = open('output.txt', 'w') 



def main():
    t=int(input())
    for _ in range(t):
        s=input()

        d=Counter(s)
        # print(d)
        l='L'
        r='R'
        u='U'
        D='D'
        if(d[l]<=d[r]):
            s1=""
            c=d[r]-d[l]
            for i in range(len(s)):
                if(c>0 and s[i]==r):
                    c-=1
                else:
                    s1+=s[i]
        elif(d[l]>d[r]):
            s1=""
            c=d[l]-d[r]
            for i in range(len(s)):
                if(c>0 and s[i]==l):
                    c-=1
                else:
                    s1+=s[i]
        if(d[D]<=d[u]):
            s2=""
            c=d[u]-d[D]
            for i in range(len(s1)):
                if(c>0 and s1[i]==u):
                    c-=1
                else:
                    s2+=s1[i]
        elif(d[D]>d[u]):
            s2=""
            c=d[D]-d[u]
            for i in range(len(s1)):
                if(c>0 and s1[i]==D):
                    c-=1
                else:
                    s2+=s1[i]

        

        d=Counter(s2)
        #print(d)
        f=0
        if(min(d[l],d[r])==0 ):
            if(min(d[u],d[D])==0):
                f=1
            else:
                f=0
        if(min(d[u],d[D])==0):
            if(min(d[l],d[r])==0 ):
                f=1
            else:
                f=0

        if("".join(list(set(list(s))))=='LR' or "".join(list(set(s[::-1])))=='LR' or "".join(list(set(list(s))))=='UD' or "".join(list(set(list(s[::-1]))))=='UD'):
            print(len("".join(list(set(list(s))))))
            print("".join(list(set(list(s)))))
        elif( (f==1 )):
            print(0)

        else:
            print(len("L"*d[l]+"U"*d[u]+"R"*d[r]+"D"*d[D]))
            print("U"*d[u]+"R"*d[r]+"D"*d[D]+"L"*d[l])






    







if __name__ == "__main__":
    main()