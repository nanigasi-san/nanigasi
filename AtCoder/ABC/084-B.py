import sys
A,B = map(int,input().split())
S = input()

if S[A]!="-":
    print("No")
    sys.exit()
try:
    a = int(S[:A])
    a = int(S[A+1:])
    print("Yes")

except:
    print("No")
