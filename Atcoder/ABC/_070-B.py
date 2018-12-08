A,B,C,D = map(int,input().split())
counter = 0
for num1 in range(A,B):
    for num2 in range(C,D):
        if num1 == num2:
            counter += 1
print(counter)
#ok
