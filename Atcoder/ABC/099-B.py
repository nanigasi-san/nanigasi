a,b = map(int,input().split())
num = b-a
sum = 0
for _ in range(num):
    sum += _+1
print(sum - b)
