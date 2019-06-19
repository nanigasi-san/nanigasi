from copy import deepcopy
import sys
from itertools import accumulate
N,X = map(int,input().split())
Llist = list(map(int,input().split()))

ruiseki = accumulate(Llist)
for i,r in enumerate(ruiseki,2):
    if r <= X:
        continue
    else:
        print(i-1)
        sys.exit()
print(i)