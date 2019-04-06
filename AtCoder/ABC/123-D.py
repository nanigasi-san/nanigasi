import sys
input = sys.stdin.readline
import numpy as np

X,Y,Z,K = map(int,input().split())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))
Clist = list(map(int,input().split()))
Alllist = [a+b+c for a in Alist for b in Blist for c in Clist]
Alllist.sort(reverse=True)

for i in range(K):
    print(Alllist[i])
