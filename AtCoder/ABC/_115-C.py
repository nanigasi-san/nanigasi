N,K = map(int,input().split())
hlist = [int(input()) for _ in range(N)]
hlist.sort(reverse=True)
sa = []

for _ in range(N-K+1):
    num = hlist[_]-hlist[_+(K-1)]
    sa.append(num)
sa.sort()
print(sa[0])
