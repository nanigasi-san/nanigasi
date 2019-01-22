N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
Asum = sum(A)
Bsum = sum(B)
yoy = []
mnu = []
test = []

if Asum < Bsum:
    flg = "NO"

else:
    flg = "YES"
    for n in range(N):
        a = A[n]
        b = B[n]
        if a >= b:
            test.append(a-b)
            yoy.append(a-b)
        else:
            test.append(a-b)
            mnu.append(a-b)
    min_num = len(mnu)#結果に足す
    min_sum = sum(mnu)#これより大きく

    yoy.sort(reverse=True)

    ynum = 0
    counter = 0
    if min_num != 0:
        for y in yoy:
            counter += 1
            ynum += y
            if ((ynum+min_sum) >= 0):
                break

if flg == "YES":
    print(min_num+counter)
else:
    print(-1)
