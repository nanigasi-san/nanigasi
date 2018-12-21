A,B = map(int,input().split())
list = [A+B,A-B,A*B]
list.sort(reverse=True)
print(list[0])
#AC
