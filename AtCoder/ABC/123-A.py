ant_list = [int(input()) for _ in range(5)]
k = int(input())
flg = True
for t in ant_list:
    for j in ant_list:
        if abs(t-j)>k:
            flg = False

if flg:
    print("Yay!")

else:
    print(":(")
