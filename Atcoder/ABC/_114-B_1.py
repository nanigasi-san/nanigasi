S = list(input())
list = []
for _ in range(len(S)-2):
    Sx = S[_]+S[_+1]+S[_+2]
    sa = int(Sx)-753
    list.append(abs(sa))
list.sort()
print(list[0])
