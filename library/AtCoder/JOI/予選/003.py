N = int(input())
S = list(input())
point = 0
sys = 0
for _ in range(N-1):
    if sys == 1:
        sys = 0
        continue
    if S[_+1] == S[_]:
        continue
    elif S[_+1] != S[_]:
        point += 1
        sys += 1
print(point)
#ok
