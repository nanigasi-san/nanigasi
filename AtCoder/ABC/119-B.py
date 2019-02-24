N = int(input())
list = [list(map(str,input().split())) for i in range(N)]
sum = 0
for ele in list:
    if ele[1]=="JPY":
        sum += int(ele[0])
    else:
        sum += (float(ele[0])*380000.0)

print(sum)
