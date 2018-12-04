N = int(input())
list = [list(map(int,input().split())) for _ in range(N)]
print(list)
a = b = 0

for i in range(N):
    ax = list[i][0]
    bx = list[i][1]
    if ax > bx:
        a += 1
    elif ax < bx:
        b += 1
print(a,b)
