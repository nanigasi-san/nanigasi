A,B,C= map(int,input().split())
sum = 0
day = 00
while sum < C:
    day += 1
    sum += A
    if day%7 == 0:
        sum += B
print(day)
#ok
