N = int(input())
list = [a for a in map(int,input().split())]
list.sort(reverse=True)
num = 0
alice = 0
bob = 0
for _ in list:
    if num == 0:
        alice += _
        num = 1
        continue
    else:
        bob += _
        num = 0
        continue
print(alice-bob)
