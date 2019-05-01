import numpy as np
N = int(input())
slist = np.array(list(map(int,input().split())))
alist = np.array(list(map(int,input().split())))

breaker = alist*slist
print(np.max(breaker))
