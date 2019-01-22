A = int(input())
B = int(input())
C = int(input())
list = [A,B,C]#順番
list_ = [A,B,C]#順位
list_.sort(reverse=True)
print(list_.index(list[0])+1)
print(list_.index(list[1])+1)
print(list_.index(list[2])+1)
#AC
