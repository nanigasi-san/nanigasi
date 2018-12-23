a,X = map(int,input().split())
alist = list(map(int,input().split()))
enp = []
while X>=1:
    enp.append(X%2)
    X = X//2
sum = 0
counter = 0
for e in enp:
    sum += alist[counter]*e
    counter += 1
print(sum)
#AC
