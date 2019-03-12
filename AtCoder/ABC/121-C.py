N,M = map(int,input().split())

ABlist = [list(map(int,input().split())) for n in range(N)]
Alist = [ab[0] for ab in ABlist]
Blist = [ab[1] for ab in ABlist]

sum = 0
flg = False
while True:
    min_ = min(Alist)
    min_index = Alist.index(min_)
    b_num = Blist[min_index]
    for i in range(b_num):
        M -= 1
        sum += min_
        if M==0:
            flg = True
            break
    Blist.remove(b_num)
    Alist.remove(Alist[min_index])
    if flg == True:
        break
print(sum)


"""
TLEwwwwwwwww
"""
