A,B,C = map(int,input().split())

if A+B==C:
    print(C+B)
elif A+B<C:
    print(A+B+1+B)
elif A+B>C:
    print(C+B)
