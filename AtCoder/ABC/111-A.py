list = list(map(int,input().split()))
list.sort()
num1 = abs(list[1]-list[0])
num2 = abs(list[2]-list[1])
print(num1+num2)
#ok
