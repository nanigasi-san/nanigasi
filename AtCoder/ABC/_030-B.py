n,m = map(int,input().split())
if n >= 12:
    n = n-12
n_,m_ = 0.5*(n*60+m),6*m
kaku1,kaku2 = n_-m_,m_-n_
if kaku1 >= kaku2:
    print(abs(kaku2))
else:
    print(abs(kaku1))
