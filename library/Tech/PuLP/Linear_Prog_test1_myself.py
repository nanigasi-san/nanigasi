import numpy as np
import matplotlib.pyplot as plt

def c(data):
    print(data)

plt.axis([0,4.5,0,8.5])

x = np.arange(0,4.6,0.1)
y1 = -(x/2)+5
plt.plot(x,y1,label="x1+2x2 <= 10")

y2 = -(2*x)+8
plt.plot(x,y2,label="2x1+x2<=8")

zeros_x = np.zeros_like(x)

mini = np.minimum(y1,y2)
plt.fill_between(x,zeros_x,mini,facecolor="g",alpha=0.3)
plt.legend(loc=0)
plt.savefig("F:/image/Linear_Prog_test1_myself.png")
plt.show()
