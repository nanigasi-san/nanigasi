S = list(input())
N = int(input())
num = 0
for x in S:
    for y in S:
        num += 1
        if num == N:
            print(x+y)
#go
