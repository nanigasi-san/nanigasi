A,B = map(int,input().split())
if A == 1:
    if B == 1:
        print("Draw")
    else:
        print("Alice")
else:
    if B == 1:
        print("Bob")
    elif A > B:
        print("Alice")
    elif A < B:
        print("Bob")
    else:
        print("Draw")
#AC
