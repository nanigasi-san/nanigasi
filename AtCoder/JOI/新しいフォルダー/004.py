N = int(input())
A = list(map(int,input().split()))
High = [n for n in range(max(A))]
High2 = []
for high in High:
    if A.count(high) != 0:
        High2.append(high)
gnum = 0
for high in High2:
    num = 0
    sw = 0
    for a in A:
        if sw == 0:
            if a-high <= 0:
                continue
            else:
                sw += 1
                num += 1
        elif sw == 1:
            if a-high <= 0:
                sw = 0

    if gnum < num:
        gnum = num

print(gnum)
