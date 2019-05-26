from collections import Counter
N = int(input())
alist = Counter(tuple(map(int,input().split())))
max_counter = 0
com = alist.most_common()
for num,cou in com:
    counter = 0
    counter += cou
    counter += alist[num-1]
    counter += alist[num+1]
    if counter > max_counter:
        max_counter = counter

print(max_counter)