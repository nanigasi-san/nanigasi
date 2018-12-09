N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
counter = 0
for i in range(A[0]+1):
    counter2 = A.count(i)
    if counter2 > counter:
        counter = counter2
print(counter)
