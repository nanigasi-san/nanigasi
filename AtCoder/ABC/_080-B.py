N = input()
Nlist = list(N)
sum = 0
for n in Nlist:
    sum += int(n)
if int(N)%sum == 0:
    print("Yes")
else:
    print("No")
#ok
