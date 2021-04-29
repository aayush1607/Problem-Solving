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
        l=int(input())
        s=input()
        lr=s.find('LR')
        rl=s.find('RL')
        ud=s.find('UD')
        du=s.find('DU')
        ruld=s.find('RULD')    
        lurd=s.find('LURD')    
        rdlu=s.find('RDLU')    
        ldru=s.find('LDRU')    
        if(lr!=-1):
            print(lr+1,lr+2)
        elif(rl!=-1):
            print(rl+1,rl+2)
        elif(ud!=-1):
            print(ud+1,ud+2)
        elif(du!=-1):
            print(du+1,du+2)
        elif(ruld!=-1):
            print(ruld+1,ruld+4)
        elif(lurd!=-1):
            print(lurd+1,lurd+4)
        elif(rdlu!=-1):
            print(rdlu+1,rdlu+4)
        elif(ldru!=-1):
            print(ldru+1,ldru+4)
        else:
            print(-1)

if __name__ == "__main__":
    main()