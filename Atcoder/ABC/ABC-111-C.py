n = int(input())
list = list(map(int,input().split()))
list1 = []
list2 = []
for i in range(0,n,2):
    list1.append(list[i])
for l in range(1,n,2):
    list2.append(list[l])
