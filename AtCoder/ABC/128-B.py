import bisect
N = int(input())
guide_dic = {}
num_i_dic = {}
for _ in range(N):
    S,P = input().split()
    num_i_dic[int(P)] = _+1
    try:
        bisect.insort(guide_dic[S],int(P))
    except KeyError:
        guide_dic[S] = []
        bisect.insort(guide_dic[S],int(P))

for name,score in sorted(guide_dic.items()):
    for _ in score[::-1]:
        print(num_i_dic[_])