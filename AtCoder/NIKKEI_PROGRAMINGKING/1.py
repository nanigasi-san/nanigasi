N,A,B = map(int,input().split())

sum = A+B
if A+B <= N:
    min = 0
else:
    min = (A+B)-N

#max
if A >= B:
    max=B
else:
    max = A

print(max,min)
