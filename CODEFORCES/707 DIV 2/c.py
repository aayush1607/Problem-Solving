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

	n=int(input())
	a=list(map(int,input().split()))
	d=Counter()
	f=0
	ac=Counter()

	for 

	for i in range(len(a)):
		for j in range(i+1,len(a)):
			d[a[i]+a[j]]=[]
			d[a[i]+a[j]].append(i)
			d[a[i]+a[j]].append(j)


	for i in d:
		if(len(d[i])>=2):
			print("YES")
			print(d[i][0][0]+1,d[i][0][1]+1,d[i][1][0]+1,d[i][1][1]+1)
			f=1
			break
	if(f==0):
		print("NO")

			




        

    







if __name__ == "__main__":
    main()