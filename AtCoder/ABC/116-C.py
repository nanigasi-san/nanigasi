import numpy as np
N = int(input())
hlist = np.array([_ for _ in map(int,input().split())])

max = np.max(hlist)
min = np.min(hlist)

newlist = np.zeros_like(hlist)
num = 0

list = []
#+++++
for i in range(1,N):
    sa = hlist[i-1]-hlist[i]
    if sa > 0:
        list.append(sa)
list.append(hlist[N-1])

print(sum(list))
