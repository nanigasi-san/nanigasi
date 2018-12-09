N = int(input())
X = list(map(int,input().split()))
M = int(input())
A = list(map(int,input().split()))

for n in A:
    try:
        if X[n-1]+1 != X[n]:
            X[n-1] += 1
    except:
        if X[n-1]+1 < 2020:
            X[n-1] += 1
for x in X:
    print(x)
    #go
