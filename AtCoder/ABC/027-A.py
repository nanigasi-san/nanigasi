l = list(map(str,input().split()))
if l.count(l[0]) != l.count(l[1]):
    if l.count(l[0]) == 1:
        print(l[0])
    else:
        print(l[1])
else:
    print(l[2])
#ac
