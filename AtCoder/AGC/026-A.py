N = int(input())
alist = list(map(int,input().split()))

counter = 0
for i in range(1,N):
    if alist[i-1]==alist[i]:
        counter += 1
        alist[i] += 10000

print(counter)
