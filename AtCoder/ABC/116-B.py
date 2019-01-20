s = int(input())
i = 1
mae = s
list = [s]
while True:
    i += 1
    if mae%2 == 0:
        y = mae/2
    else:
        y = 3*mae+1
    mae = y
    if list.count(y) == 1:
        print(i)
        break
    list.append(y)
