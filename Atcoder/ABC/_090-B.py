A,B = map(int,input().split())
counter = 0
for _ in range(A,B+1):
    str = str(_)
    alist = list(str)
    print(alist)
    list_ = []
    long = len(alist)
    for i in range(long-1,-1,-1):
        list_.append(alist[i])
    num = "".join(list_)
    if num == str:
        counter += 1
        continue
    else:
        continue

print(counter)
