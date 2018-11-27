import sys
N = int(input())
list = list(map(int,input().split()))

num = 0
while True:
    fnum = 0
    for i in list:
        a = i/2
        a_ = int(a)
        if a != a_ :
            print(num)
            sys.exit()
        elif a == 0:
            print(num)
            sys.exit()
        else:
            list[fnum] = a
            fnum += 1
    num += 1

print(num)
