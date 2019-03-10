N,M,C = map(int,input().split())
Blist = list(map(int,input().split()))
Alist = [list(map(int,input().split())) for i in range(N)]
counter = 0
for x in range(N):
    all = C
    xlist = Alist[x]
    for j in range(M):
        all += Blist[j]*xlist[j]
    if all>0:
        counter += 1
print(counter)
