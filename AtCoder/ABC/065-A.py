X,A,B = map(int,input().split())
if A >= B:#umai
    print("delicious")
elif A < B:#mazui
    over = B-A
    if over <= X:
        print("safe")
    else:
        print("dangerous")
#ok
