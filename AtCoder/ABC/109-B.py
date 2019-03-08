N = int(input())
W_list = [input() for _ in range(N)]
mae = W_list[0]
flg = "Yes"
for w in W_list[1:]:
    if mae[-1]==w[0]:
        mae = w
    else:
        flg = "No"
W_set = set(W_list)
if len(W_list)!=len(W_set):
    flg = "No"

print(flg)
