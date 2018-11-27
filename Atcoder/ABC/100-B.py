#yet
D,N = map(int,input().split())
list =[]
num = 0
for i in range(1,1000001):
    if i%100**D == 0:
        list.append(i)
print(list[N-1])
#go
