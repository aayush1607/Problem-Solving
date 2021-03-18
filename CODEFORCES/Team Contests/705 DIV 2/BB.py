import os
import sys
from collections import Counter
from io import BytesIO, IOBase
import math

BUFSIZE = 8192

if sys.version_info[0] < 3:
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


def print(*args, **kwargs):
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


def checkR(hm, r):
    if (0 <= hm < r):
        return True
    return False


def checkN(ss,r):
    d = {'0': '0', '1': '1', '2': '5', '8': '8', '5': '2'}
    nss = ""
    f = 0
    for i in ss:
        if (i in d):
            nss += d[i]
        else:
            f = 1
            break
    if (f == 1):
        return False
    else:
    	nss=nss[::-1]

    	if(checkR(int(nss),r)):
            return True
    	return False


# def checkN(ss):
# 	d={'0':'0','1':'1','2':'5','8':'8','5':'2'}
# 	nss=""
# 	f=0
# 	for i in ss:
# 		if(i in d):
# 			nss+=d[i]
# 		else:
#    			f=1
#    			break
#    	if(f==1):
#    		return False
#    	else:
#    		return True

# For getting input from input.txt file 
sys.stdin = open('in.txt', 'r')  
  
# Printing the Output to output.txt file 
sys.stdout = open('ou.txt', 'w') 
def main():
    t = int(input())
    for _ in range(t):
        h, m = map(int, input().split())
        hh, mm = input().split(':')
        #print(hh,mm)
        while (checkN(mm,h) == False):
            
            mm = int(mm) + 1
            
            if (checkR(mm, h)):
                
                mm = str(mm)
                if (len(mm) == 1):
                    mm = "0" + mm
            else:
                mm = 0
                mm = str(mm)
                if (len(mm) == 1):
                    mm = "0" + mm
                print("#mm",mm)
                hh = int(hh) + 1
                if (checkR(hh, m)):
                    hh = str(hh)
                    if (len(hh) == 1):
                        hh = "0" + hh
                else:
                    hh = h
                    hh = str(hh)
                    if (len(hh) == 1):
                        hh = "0" + hh

        while (checkN(hh,m) == False):
            #print("#hh",hh)
            hh = int(hh) + 1
            
            if (checkR(hh, m)):
                hh = str(hh)
                if (len(hh) == 1):
                    hh = "0" + hh
            else:
                hh = 0
                hh = str(hh)
                if (len(hh) == 1):
                    hh = "0" + hh

        # if(checkN(hh,h)==False or checkN(mm,m)==False):
        # 	print("00:00")
        # else:
        print(hh + ":" + mm)


    # nmm=""
    # f=0
    # for i in mm:
    # 	if(i in d):
    # 		nmm+=d[i]
    # 	else:
    # 		#print("00:00")
    # 		f=1
    # 		break
    # if(f==0):
    # 	nmm=nmm[::-1]
    # 	new_hh=nmm
    # 	nhh=""
    # 	for i in hh:
    # 		if(i in d):
    # 			nhh+=d[i]
    # 		else:
    # 			#print("00:00")
    # 			f=1
    # 			break
    # 	if(f==0):
    # 		new_mm=nhh[::-1]
    # 		if(0<=int(new_mm)<mm) and 0<=int(new_hh)<hh):
    # 			print(hh+":"+mm)
    # 		else:
    # 			print("00:00")


if __name__ == "__main__":
    main()