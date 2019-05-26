N,M = map(int,input().split())
LRlist = [tuple(map(int,input().split())) for _ in range(M)]

min_n = 0
max_n = N
for l,r in LRlist:
    min_n = l if l>min_n else min_n
    max_n = r if r<max_n else max_n

ans = max_n-min_n+1
print(ans if ans>0 else 0)