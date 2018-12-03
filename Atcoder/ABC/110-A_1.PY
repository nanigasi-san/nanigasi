list = list(map(str,input().split()))
list.sort(reverse=True)
A = list[0]+list[1]
B = list[2]
print(int(A)+int(B))
