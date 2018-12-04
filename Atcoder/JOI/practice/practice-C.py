N = int(input())
a = list(map(str,input().split()))
a_ = []
for i in range(N,0,-1):
    ii = a[i-1]
    a_.append(ii)
print(" ".join(a_))
