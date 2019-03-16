N,x = map(int,input().split())
alist = list(map(int,input().split()))
alist.sort()
counter = 0
for i in range(N):
    x -= alist[i]
    if x>=0:
        if i!=N-1:
            counter += 1
        else:
            if x==0:
                counter += 1
    else:
        break
print(counter)
