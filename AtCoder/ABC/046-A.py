list = list(map(int,input().split()))
if list.count(list[0]) == 3:
    print(1)
elif list.count(list[0]) == 2:
    print(2)
else:
    if list[1] == list[2]:
        print(2)
    else:
        print(3)
