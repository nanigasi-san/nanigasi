N = int(input())

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

tmplist = [A,B,C,D,E]
max_time_list = []
for x in tmplist:
    dim = N/x
    max_time_list.append(int(dim)+1 if int(dim)!=dim else int(dim))

print(max(max_time_list)+4)
