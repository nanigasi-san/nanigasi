A,B,C = map(int,input().split())
if A+B == C:
    if A-B == C:
        print("?")
    else:
        print("+")
else:
    if A-B == C:
        print("-")
    else:
        print("!")
#AC
