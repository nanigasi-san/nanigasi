import numpy as np

N,M = map(int,input().split())
Xlist = np.array([int(_) for _ in input().split()])
Xlist = np.sort(Xlist)
answer = 0
max_difflist = np.array([])
salist = np.array([])
ilist = np.array([])
min_n = -1

for i in range(M-1):
    sa = abs(Xlist[i]-Xlist[i+1])
    salist = np.append(salist,sa)

    if len(max_difflist)+1 < N:
        ilist = np.append(ilist,i)
        max_difflist = np.append(max_difflist,sa)

    elif sa > min_n:
        max_difflist = np.sort(max_difflist)[::-1]
        index = np.where(max_difflist == min_n)[0]
        max_difflist[index] = sa
        ilist[index] = i
    min_n = np.min(max_difflist)

for i_ in ilist:
    salist[int(i_)] = 0

print(int(sum(salist)))
