c0 = list(map(str,input().split()))
c1 = list(map(str,input().split()))
c2 = list(map(str,input().split()))
c3 = list(map(str,input().split()))

list = [c0+c1+c2+c3]
print(list)
list2 = []
for i in range(len(list),0):
    list2.append(list[i-1])
counter = 0
for x in range(4):
    print(list2[x+counter],list2[x+1+counter],list2[x+2+counter],list2[x+3+counter])
    counter += 4
