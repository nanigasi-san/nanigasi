list = []
for n in range(int(input())):
    A = int(input())
    if list.count(A) == 0:
        list.append(A)
list.sort(reverse=True)
print(list[1])
#ac
