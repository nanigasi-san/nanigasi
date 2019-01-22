N = list(input())
if N.count(N[0]) == 3 and N[3] != N[0]:
    print("Yes")
elif N.count(N[0]) == 4:
    print("Yes")
elif N.count(N[3]) == 3 and N[3] != N[0]:
    print("Yes")
else:
    print("No")
#AC
