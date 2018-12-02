#約数を出すプログラム
N = int(input())
counter = 0
for _ in range(N):
    waru = _+1
    if N%waru == 0:
        counter += 1

print(counter)
