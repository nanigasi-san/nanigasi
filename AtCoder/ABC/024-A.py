A,B,C,K = map(int,input().split())
S,T = map(int,input().split())
if S+T >= K:
    A -= C
    B -= C
print(A*S+B*T)
#ac
