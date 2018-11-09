import numpy as np
import matplotlib.pyplot as plt
plt.figure()


LX = 2.1
LY = 2.1
gridwidth = 0.33

X,Y = np.meshgrid(np.arange(-LX,LX,gridwidth),np.arange(-LY,LY,gridwidth))
R = np.sqrt(X**2+Y**2)

X1,Y1 = 0,0
plt.plot(X1,Y1,'o',color='blue')

Q = 1
R1 = np.sqrt((X-X1)**2+(Y-Y1)**2)

#ベクトル関数の定義
U = Q*(X-X1)/(R1**2)
V = Q*(Y-Y1)/(R1**2)
plt.quiver(X,Y,U,V,color='red',angles='xy',scale_units='xy',scale=5.0)
plt.xlim([-LX,LX])
plt.ylim([-LY,LY])

plt.grid()
plt.draw()
plt.show()
