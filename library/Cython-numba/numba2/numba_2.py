import numpy as np
import time
t1 = time.time()
def test():
    A = np.array([[np.ones(10**5),np.zeros(10**5)],[np.ones(10**5),np.zeros(10**5)]])
    for x in range(10**5):
        a = A[0][0][x]+A[0][1][x]+A[1][0][x]+A[1][1][x]
for i in range(100):
    test()
print("loop=",i+1)
t2 = time.time()
print("time =",t2-t1)
t1 = time.time()
