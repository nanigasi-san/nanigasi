import sys
N,T = map(int,input().split())
min = 1000
index = 0
min_index = ""

for _ in range(N):
    index += 1
    c,t = map(int,input().split())

    if t <= T and c <= min:
        min = c
        min_index = index

if min_index == "":
    print("TLE")
    sys.exit()
print(min_index)
