#yet
N = int(input())
M = N-1
n = N//2
m = M//2
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)
A_ = []
num = 0

if N >= 4:
    A_.append(A[n])
    for _ in range(m):
        A_.append(A[_])
        A_.append(A[M-_])
    if n != m:
        A_.append(A[m])#A_完了
    for _ in range(M):
        num += (abs((A_[_])-(A_[_+1])))
    print(num)
elif N == 3:
    A[1],A[2] = A[2],A[1]
    abs1 = abs(A[0]-A[1])
    abs2 = abs(A[1]-A[2])
    print(abs1+abs2)

else:
    print(A[0]-A[1])
