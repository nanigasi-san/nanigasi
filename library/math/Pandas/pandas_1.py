#-----------
def fin():
    print("="*30)
#-----------
import pandas as pd
import numpy as np

s = pd.Series(data = np.random.randint(1,7,100),index = range(0,100))

print(s)
fin()

print(s[1])
fin()

print(s[1:4])
fin()

print(s.head(3))
fin()

print(s.tail(3))
fin()

fig = s.plot(kind='bar').get_figure()
fig.savefig("figurel.png")

print(s.describe())
#上から
#count-> データの数
#mean-> 中央値
#std-> 不偏標準偏差
#min-> 最小値
#25%-> 最小値から25%の位置にある値
#50%-> 最小値から50%の位置にある値
#75%-> 最小値から75%の位置にある値
#max-> 最大値
