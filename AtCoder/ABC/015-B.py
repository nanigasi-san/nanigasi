N = int(input())
num = 0
A_ = list(map(int,input().split()))
A = []
for a_ in A_:
    if a_ != 0:
        num += 1
        A.append(a_)
sum = 0
for a in A:
    sum += a
ans = sum/num
ans2 = int(sum/num)
if ans > ans2:
    ans2 += 1

print(ans2)
#AC
