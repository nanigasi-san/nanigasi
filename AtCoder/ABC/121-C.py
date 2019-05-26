N,M = map(int,input().split())
ABlist = [tuple(map(int,input().split())) for _ in range(N)]
ABlist.sort()
money = 0
for AB in ABlist:
    maz_num = AB[1]
    maz_pri = AB[0]
    add_m = maz_pri*maz_num
    if M > 0:
        money += add_m
        M -= maz_num
    if M == 0:
        break
    if M < 0:
        while M!=0:
            money -= maz_pri
            M += 1
        break

print(money)