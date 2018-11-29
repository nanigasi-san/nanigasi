A,B,C = map(str,input().split())
a = list(A)
b = list(B)
c = list(C)
a_ = len(a)
b_ = len(b)
if a[a_-1] == b[0]:
    if b[b_-1] == c[0]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
#go
