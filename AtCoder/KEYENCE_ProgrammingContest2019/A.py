Nlist = list(map(int,input().split()))
counter = 0
if Nlist.count(1) == 1:
    if Nlist.count(9) == 1:
        if Nlist.count(7) == 1:
            if Nlist.count(4) == 1:
                counter = 1
                print("YES")
if counter == 0:
    print("NO")
