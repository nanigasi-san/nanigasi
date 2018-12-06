N = int(input())
T = list(map(int,input().split()))
M = int(input())
list = [list(map(int,input().split())) for _ in range(M)]
for _ in range(M):
    T_ = [x for x in T]
    T_[list[_][0]-1] = list[_][1]
    num = 0
    for t in T_:
        num += t
    print(num)
#ok
