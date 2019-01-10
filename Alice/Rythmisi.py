#被り防止でいきってギリシャ語つかおう
import sympy as sp
#ギリシャ語で「集合」らしい
sp.var("a:z")

def dimiourgia(list_obj=[]):#集合の生成
    if isinstance(list_obj,list) == True:
        return sp.FiniteSet(*list_obj)

def meros(oya,joukenn):#部分集合の生成
    emp = []
    for i in oya:
        ans = joukenn.subs(x,i)
        if ans == True:
            emp.append(i)
    return sp.FiniteSet(*emp)
