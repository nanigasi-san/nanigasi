H,W = map(int,input().split())
alist = [input() for _ in range(H)]

print("#"*(W+2))
for element in alist:
    print("#"+element+"#")
print("#"*(W+2))
