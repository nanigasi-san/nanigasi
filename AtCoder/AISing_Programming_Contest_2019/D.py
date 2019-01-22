import numpy as np
N,Q = map(int,input().split())
Alist_z = np.array(list(map(int,input().split())))
Qlist = [int(input()) for _ in range(Q)]


for q in Qlist:
    TAKA = []
    Alist = Alist_z
    if N%2 == 0:
        kais = N//2
        for i in range(kais):
            max = Alist.max()
            TAKA.append(max)
            Alist = Alist[~(Alist==max)]
            sa = abs(Alist-q)
            min = sa.min()
            ind = np.where(sa == min)
            dlt = Alist[ind[0][0]]
            Atest = list(Alist)
            Atest.remove(dlt)
            Alist = np.array(Atest)
    else:
        kais = N//2
        for i in range(kais):
            max = Alist.max()
            TAKA.append(max)
            Alist = Alist[~(Alist==max)]
            sa = abs(Alist-q)
            min = sa.min()
            ind = np.where(sa == min)
            dlt = Alist[ind[0][0]]
            Atest = list(Alist)
            Atest.remove(dlt)
            Alist = np.array(Atest)
        TAKA.append(Alist[0])
    print(sum(TAKA))
