import numpy as np

#一次元配列
a = np.array([1,2,3])
a

print(a)

type(a)

a.shape

#二次元配列
b = np.array([[1,2,3],[4,5,6]])
b

b.shape

#変形
c1 = np.array([0,1,2,3,4,5])
c1

c2 = c1.reshape((2,3))
c2

c3 = c2.ravel()
c3

c4 = c2.flatten()
c4

#dtype
a.dtype

d = np.array([1,2],dtype=np.int16)
d

d.dtype

d.astype(np.float16)

#インデックスとスライス
a

a[0]

a[1:]

a[-1]

b

b[0]

b[1,0]

b[:,2]

b[1,:]
