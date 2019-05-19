N,K = map(int,input().split())
res = 0
for i in range(1,N+1):
    counter = 0
    while i < K:
        counter += 1
        i *= 2
    res += (2**(-counter))
print((1/N)*res)