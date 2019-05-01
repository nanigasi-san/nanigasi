N = int(input())
Alist = [int(input()) for _ in range(N)]

counter = 0
alr_list = []
for i in range(N):
    if alr_list.count(Alist[i])>=1:
        counter += 1
    alr_list.append(Alist[i])
print(counter)