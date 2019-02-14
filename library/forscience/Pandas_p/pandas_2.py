#-----------
def fin():
    print("="*30)
#-----------
import pandas as pd
import numpy as np

d = pd.DataFrame(data=[(np.sin(2*np.pi*i/360),np.cos(2*np.pi*i/360)) for i in range(0,360)], columns=("sin","cos"), index=range(0,360))
print(d)
fin()

fig = d.plot().get_figure()
fig.savefig("figure2.png")
fin()

print(d[1:3])
fin()

print(d.head(2))
fin()

print(d.tail(2))
fin()

print(d.describe())
fin()
