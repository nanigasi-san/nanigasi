a = int(input())
b = int(input())
n = int(input())
if a >= b:
    for i in range(100000):
        A = a*i
        if A%b == 0 and A >= n:
            print(A)
            break
else:
    for i in range(100000):
        B = b*i
        if B%a == 0 and B >= n:
            print(B)
            break
#AC
