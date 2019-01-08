%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

Pi = sp.S.Pi # 円周率
E = sp.S.Exp1 # 自然対数の底
I = sp.S.ImaginaryUnit # 虚数単位

def reset(axis_data): #ユーザーでグラフの表示範囲を設定する
    print("setting:reset")
    for n in range(len(axis_data)):
        axis_data[n] = int(input(axis_data[n]+">>"))

def usedefult(axis_data): #デフォルト値(-10~10)を使う
    print("setting:defult")
    axis_data[0:4] = -10,10,-10,10

def setting(): #範囲指定をするかの選択
    print("グラフの設定をしますか？")
    axis_ = ["xmin","xmax","ymin","ymax"]

    if input("[yes/no]") == "yes":
        reset(axis_)
    else : #yes/noすら打てない人たまにいるので
        usedefult(axis_)

    global x_min,x_max
    x_min = axis_[0]
    x_max = axis_[1]+0.1

    plt.axis(axis_)
    plt.axhline(0,c='black',lw=2)
    plt.axvline(0,c='black',lw=2)
    plt.plot(0,0,'o',c='black')
    plt.grid()

def plot(step=0.1): #グラフをplotする
    x = sp.Symbol('x')
    f = sp.sympify(input("f>>"))
    y = []
    x_ = np.arange(x_min,x_max,step)
    for i in x_:
        f_ = f.subs(x,i)
        y.append(f_)
    plt.plot(x_,y,label=f)
    plt.legend()
    plt.show()

try:
    setting()
    plot()
except:
    print("ERROR")
