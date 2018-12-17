A = int(input())
max = 0
for i in range(A):
    x = i * (A-i)
    if x > max:
        max = x

print(max)
#ac
