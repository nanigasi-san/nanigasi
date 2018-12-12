N = int(input())
A = [i for i in map(int,input().split())]
count = 0
for a in A:
    while True:
        harf = a/2
        if harf == int(harf):
            a = harf
            count += 1
            continue
        else:
            break
print(count)
#ok
