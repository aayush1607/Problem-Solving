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
        n=int(input())
        mat=[]
        for i in range(n):
            l=list(input())
            mat.append(l)
        c=0
        for i in range(n):
            for j in range(n):
                if(mat[i][j]=='*'):
                    if(c==0):
                        i1=i
                        j1=j
                        c+=1
                    else:
                        i2=i
                        j2=j
                        break
        if(i1<i2 and j1<j2):
            # print(i1,i2,j1,j2)
            mat[i2][j1]='*'
            mat[i1][j2]='*'
        elif(i1<i2 and j1>j2):
            mat[i1][j2]='*'
            mat[i2][j1]='*'
        elif(j1==j2):
            mat[i1][(j1+1)%len(mat[i1])]='*'
            mat[i2][(j2+1)%len(mat[i2])]='*'
        else:
            mat[(i1+1)%n][j1]='*'
            mat[(i2+1)%n][j2]='*' 
        for i in mat:
            for j in i:
                print(j,end="")
            print()
        # print("-------------")




if __name__ == "__main__":
    main()