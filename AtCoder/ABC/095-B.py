N,X = map(int,input().split())
mlist = [int(input()) for _ in range(N)]

print(N+(X-sum(mlist))//min(mlist))