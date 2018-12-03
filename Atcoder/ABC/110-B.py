N,M,X,Y = map(int,input().split())
x = [_ for _ in map(int,input().split())]
y = [_ for _ in map(int,input().split())]
Z = [z for z in range(-100,101)]
x.sort(reverse=True)
y.sort()
num = 0

for z in Z:
    if X<z and z<=Y:
        if x[0]<z and y[0]>=z:
            print('No War')
            num += 1
            break
    else:
        continue
if num == 0:
    print('War')
