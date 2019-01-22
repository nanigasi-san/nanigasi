N,T = map(int,input().split())
ctlist = [list(map(int,input().split())) for _ in range(N)]

minimum_cost = 1001

for sub_list in ctlist:
    if sub_list[1] <= T:
        if sub_list[0] < minimum_cost:
            minimum_cost = sub_list[0]

if minimum_cost == 1001:
    print("TLE")
else:
    print(minimum_cost)
