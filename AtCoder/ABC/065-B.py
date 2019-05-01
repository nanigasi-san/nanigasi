N = int(input())
alist = [int(input()) for _ in range(N)]

now = alist[0]
for i in range(N):
    if now==2:
        print(i+1)
        break
    now = alist[now-1]
else:
    print(-1)
