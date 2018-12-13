N = int(input())
list = []
maxname = ""
maxtime = 0
for n in range(N):
    list.append(input())
for _ in list:
    cou = list.count(_)
    if cou > maxtime:
        maxtime = cou
        maxname = _
print(maxname)
#ac
