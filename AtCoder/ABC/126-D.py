import numpy as np
N = int(input())
colorlist = np.array([True for _ in range(N+1)])
datalist = []
for i in range(N-1):
    data = tuple(map(int,input().split()))
    datalist.append(data)


for data in datalist:
    if data[2]%2 != 0:
        colorlist[data[1]] = not colorlist[data[0]]

for a in colorlist.astype(np.int)[1:]:
    print(a)