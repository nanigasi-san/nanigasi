A,B = map(int,input().split())
counter = 0
for _ in range(A,B+1):
    str = str(_)
    alist = list(str)
    list_ = []
    long = len(alist)
    for i in range(long-1,-1,-1):
        list_.append(alist[i])
    num = "".join(list_)
    if str(num) == str:
        counter += 1

print(counter)
#?????
