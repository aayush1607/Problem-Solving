import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from collections import Counter
from collections import defaultdict as dd

# sys.setrecursionlimit(100000000)

flush = lambda: stdout.flush()
stdstr = lambda: stdin.readline()
stdint = lambda: int(stdin.readline())
stdpr = lambda x: stdout.write(str(x))
stdmap = lambda: map(int, stdstr().split())
stdarr = lambda: list(map(int, stdstr().split()))

mod = 1000000007

for _ in range(stdint()):
    n, u, r, d, l = stdmap()

    l = [u, r, d, l]

    pos = True
    for i in range(4):
        p, ne = l[(i - 1) % 4], l[(i + 1) % 4]
        opp = l[(i + 2) % 4]
        if (l[i] == 0):
            if (p == n or ne == n):
                pos = False
                break
            elif(p == n-1 and ne == n-1 and opp == 1):
                pos = False
                break
            elif ((p == n - 1 or ne == n - 1) and opp == 0):
                pos = False
                break
        elif (l[i] == 1):
            if (p == n and ne == n):
                pos = False
                break
            else:
                if ((p == n or ne == n) and (p == n - 1 or ne == n - 1) and opp <= 1):
                    pos = False
                    break

    if (pos):
        print("YES")
    else:
        print("NO")

