N = int(input())
D,X = map(int,input().split())
Alist = [int(input()) for _ in range(N)]

choco = 0
for i in range(N):
    day = 1
    while day <= D:
        choco += 1
        day += Alist[i]

print(choco+X)
