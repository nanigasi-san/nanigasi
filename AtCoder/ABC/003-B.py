c0 = list(map(str,input().split()))
c1 = list(map(str,input().split()))
c2 = list(map(str,input().split()))
c3 = list(map(str,input().split()))

list = c0+c1+c2+c3
list2 = []
for i in range(len(list),0,-1):
    list2.append(list[i-1])
counter = 0
for i in range(4):
    xxx = i+counter
    print(list2[xxx],list2[xxx+1],list2[xxx+2],list2[xxx+3])
    counter += 3
#ac
