N = int(input())
A,B = map(int,input().split())
plist = [int(_) for _ in input().split()]


a,b,c = 0,0,0
list = []
for p in plist:
    if p <= A:
        a += 1
    elif A+1 <= p <= B:
        b += 1
    elif B+1 <= p:
        c += 1

list.append(a)
list.append(b)
list.append(c)

print(min(list))
