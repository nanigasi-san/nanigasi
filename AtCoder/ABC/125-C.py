from copy import copy
N = int(input())
Alist = list(map(int,input().split()))
all_list = []

def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd(b,a%b)

def gcd_list(number_list):
    res = number_list[0]
    for c in number_list[1:]:
        res = gcd(res , c)
    return res

for i in range(N):
    a_list = copy(Alist)
    a_list.pop(i)
    all_list.append(gcd_list(a_list))

print(max(all_list))
