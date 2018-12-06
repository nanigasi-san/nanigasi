A,B,C = map(int,input().split())
A_ = A
counter = 0
while True:
    if A_%B == C:
        print("YES")
        break
    A_ += A
    counter += 1
    if counter > B:
        print("NO")
        break
#なんか知らんが動いた！
#ok
