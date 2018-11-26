N = int(input())
number = [int(i) for i in input().split()]
print(number)
re = 0
for num in number:
    if num%2 == 0:
        num = num/2
        re += 1
    else:
        print(re)
        break
