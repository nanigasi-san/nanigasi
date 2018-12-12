A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A >= B:
    if C >= D:
        print(B+D)
    else:
        print(B+C)
else:
    if C >= D:
        print(A+D)
    else:
        print(A+C)
#ok
