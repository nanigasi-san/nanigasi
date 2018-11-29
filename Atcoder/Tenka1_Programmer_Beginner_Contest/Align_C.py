#yet
N = int(input())
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)
A_ = ["X"]
print(A)
a = 0
b = 0
if N % 2 != 0:
    while b+2 <= N:
        A_.append(A[a])
        a += 1
        A_.append(A[N-a])
        b += 2
    A_[0] = A[a]
print(A_)
ABS = 0
for _ in range(N):
    ABS += abs(A_[_]-A_[_+1])
print(ABS)
