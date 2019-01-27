N = int(input())
A=list(input())
B=list(input())
C=list(input())

count = 0

for i in range(N):
    flg = A[i]
    if flg==B[i]:
        if flg==C[i]:
            continue
        else:
            count += 1
            continue
    else:
        if flg==C[i]:
            count+=1
        else:
            if B[i]==C[i]:
                count += 1
            else:
                count += 2
print(count)
