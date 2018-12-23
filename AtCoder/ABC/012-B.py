N = int(input())

s,m, = N%60,N//60
m_,h = m%60,m//60

if s < 10:
    S = "0"+str(s)
else:
    S = str(s)

if m_ < 10:
    M = "0"+str(m_)
else:
    M = str(m_)

if h < 10:
    H = "0"+str(h)
else:
    H = str(h)
print(H+":"+M+":"+S)
#AC
