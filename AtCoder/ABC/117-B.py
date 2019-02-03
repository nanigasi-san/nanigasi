N = int(input())
Llist = [int(_) for _ in input().split()]
max = max(Llist)
sa = sum(Llist)

ama = sa-max
if max < ama:
    print("Yes")

else:
    print("No")
