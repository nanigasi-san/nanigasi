N = int(input())
list = [int(input()) for _ in range(N)]
list.sort(reverse=True)
list[0] = list[0]/2
sum = 0
for _ in list:
    sum += _
print(int(sum))
