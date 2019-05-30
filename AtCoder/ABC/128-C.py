from copy import deepcopy
N,M = map(int,input().split())
s_list = []
for _ in range(M):
    s_list.append(tuple(map(int,input().split()[1:])))
plist = tuple(map(int,input().split()))

counter = 0
TF = [0]*N
TFlist = []
def make_bbb(long,number):
    b_n = bin(number)[2:]
    bbb = "0"*(long-len(b_n))+b_n
    return bbb
for _ in range(2**N):
    number = list(map(int,list(make_bbb(N,_))))
    TFlist.append(number)


for TF in TFlist:
    flg = False
    ok = 0
    for num,s in enumerate(s_list):
        sum_on = 0
        #各スイッチ
        for ele in s:
            sum_on += TF[ele-1]
        if sum_on%2 != plist[num]:
            flg = False
            break
        else:
            ok += 1
    if ok == M:
        counter += 1


print(counter)