A,B,K = map(int,input().split())

count_list = [i for i in range(1,101) if A%i==0 and B%i==0]
print(count_list[-K])
