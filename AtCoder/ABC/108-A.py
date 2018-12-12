K = int(input())
gu = []
ki = []
for i in range(1,K+1):
    if i%2 == 0:
        gu.append(i)
    else:
        ki.append(i)

print(len(gu)*len(ki))
#ok
