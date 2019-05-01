import numpy as np
N = int(input())
Vlist = np.array(list(map(int,input().split())))
Clist = np.array(list(map(int,input().split())))

Dlist = Vlist-Clist

sum_ = 0
for d in Dlist:
    if d >= 0:
        sum_ += d

print(sum_)
