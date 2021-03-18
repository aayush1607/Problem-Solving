
from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase
from collections import Counter
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

def check(s,a,b,c):
    ss=""
    d=Counter()
    d['A']=a
    d['B']=b
    d['C']=c
    for i in s:
        ss+=d[i]
    open_list = ["("] 
    close_list = [")"]
    
    # Function to check parentheses 
    stack = [] 
    for i in ss: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return False
    if len(stack) == 0: 
        return True
    else: 
        return False

def main():
    t=int(input())
    for _ in range(t):
        a=input()
        f=0
        if(a[0]=='A'):
            A="("
            if(check(a,A,")",")") or check(a,A,")","(") or check(a,A,"(",")")):
                f=1

        if(a[0]=='B'):
            B="("
            if(check(a,")",B,")") or check(a,"(",B,")") or check(a,")",B,"(")):
                f=1
        if(a[0]=='C'):
            C="("
            if( check(a,")",")",C) or check(a,"(",")",C) or check(a,")","(",C)):
                f=1
        if(f==1):
            print("YES")
        else:
            print("NO")


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


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
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
# zz=not __debug__
# if not zz:
#     sys.stdin=open('input.txt', 'r')
#     sys.stdout=open('output.txt','w')
# endregion

if __name__ == "__main__":
    main()