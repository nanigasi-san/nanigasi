A = int(input())
B = int(input())
C = int(input())
list,copy = [A,B,C],[A,B,C]
list.sort(reverse=True)
print(copy.index(list[0])+1)
print(copy.index(list[1])+1)
print(copy.index(list[2])+1)
