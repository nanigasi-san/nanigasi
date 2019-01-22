counter = 0
out = [2,4,5,6,8]
n = int(input())
alist = list(map(int,input().split()))
for a in alist:
    while out.count(a):
        a -= 1
        counter += 1
print(counter)
#AC
