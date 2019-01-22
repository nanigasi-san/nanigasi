A,B =map(int,input().split())
count = 0
if A%3==0:
    print("Possible")
    count += 1
if B%3==0:
    if count == 0:
        print("Possible")
        count += 1
if (A+B)%3==0 :
    if count == 0:
        print("Possible")
        count += 1
if count == 0:
    print("Impossible")
#AC
