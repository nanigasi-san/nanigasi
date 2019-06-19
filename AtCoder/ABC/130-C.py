W,H,x,y = map(int,input().split())

all_menseki = W*H
if x==W/2:
    if y==H/2:
        print(all_menseki/2,1)
    else:
        print(all_menseki/2,0)
else:
    print(all_menseki/2,0)