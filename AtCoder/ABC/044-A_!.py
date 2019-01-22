N = int(input())
K = int(input())
X = int(input())
Y = int(input())

sum = 0
if N <= K:
    print(X*N)
elif N > K:
    print(X*K+(N-K)*Y)
#ok
