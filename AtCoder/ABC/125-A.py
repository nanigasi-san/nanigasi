A,B,T = map(int,input().split())

count = 0
a_ = A

while a_ <= T+0.5:
    count += B
    a_ += A

print(count)
