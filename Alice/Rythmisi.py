#被り防止でいきってギリシャ語つかおう
#ギリシャ語で「集合」らしい
import sympy as sp
x = sp.Symbol("x")
class Dimiourgia():

    def olokliro(self,list_obj=[]):#集合の生成
        if isinstance(list_obj,list) == True:
            return sp.FiniteSet(*list_obj)

    def meros(self,oya,joukenn):#部分集合の生成
        emp = []
        for i in oya:
            ans = joukenn.subs(x,i)
            if ans == True:
                emp.append(i)
        return sp.FiniteSet(*emp)
