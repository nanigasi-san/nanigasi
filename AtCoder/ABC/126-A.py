easy_dic = {"A":"a","B":"b","C":"c"}
N,K = map(int,input().split())
S = list(input())
S[K-1] = easy_dic[S[K-1]]
print("".join(S))
