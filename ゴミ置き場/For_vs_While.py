import time
def whiletime():
    t1 = time.time()
    i = 0
    while i != 10**8:
        i += 1
    t2 = time.time()
    return t2-t1

def fortime():
    t1 = time.time()
    for i in range(10**8):
        pass
    t2 = time.time()
    return t2-t1

print(whiletime(),fortime())

#6.583530902862549 2.443481922149658
