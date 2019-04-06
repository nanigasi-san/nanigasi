A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
alist = [A,B,C,D,E]
A_=10-A%10
B_=10-B%10
C_=10-C%10
D_=10-D%10
E_=10-E%10

mlist = [A_,B_,C_,D_,E_]
for i,m in enumerate(mlist):
    if m==10:
        mlist[i]=0
min_index = mlist.index(max(mlist))

for i in range(5):
    if i!=min_index:
        alist[i]+=mlist[i]
print(sum(alist))
