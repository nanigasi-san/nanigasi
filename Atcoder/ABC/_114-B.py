S = list(input())
list = []
for _ in range(len(S)-2):
    num = S[_]+S[_+1]+S[_+2]
    list.append(int(num))
list2 = []
for _ in list:
    list2.append(abs(753-_))
list2.sort()
print(list2[0])
