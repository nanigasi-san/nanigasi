n = int(input())
nlist = list(map(int,input().split()))
print(nlist)
num = 0
for _ in nlist:
    if (_-1)%6==0 or (_-3)%6==0:
        pass
    else:
        for i in range(1,4):
            x = _-i
            if (x-1)%6==0 or (x-3)%6==0:
                num += i
                break

print(num)
#go
