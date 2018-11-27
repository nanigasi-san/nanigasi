x = input()
X = list(x)
X_ = [int(i) for i in X]
num = 0
for i in X_:
    num += i
x = int(x)
if x%num == 0:
    print("Yes")
else:
    print("No")
