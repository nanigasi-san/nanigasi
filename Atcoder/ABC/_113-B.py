N = int(input())
T,A = map(int,input().split())
H = [h for h in map(int,input().split())]
list = []
for _ in H:
    kion = T-(_*0.006)
    sa = abs(A-kion)
    list.append(sa)
list2 = [x for x in list]
list.sort()
best = list[0]
print(list2.index(best)+1)
