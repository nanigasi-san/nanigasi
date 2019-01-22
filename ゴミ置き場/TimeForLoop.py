import time
from tqdm import tqdm

def InN(n):
    def CountLoopTime(n):
        t1 = time.time()
        for _ in range(n):
            pass
        t2 = time.time()
        x = float(t2-t1)
        x = round(x,3)
        return x

    list = []
    for i in tqdm(range(n)):
        list.append(CountLoopTime(10**8))

    sum = 0
    for _ in list:
        sum += _
    ave = sum/n
    print(round(ave,3),"[s]")

InN(100)
