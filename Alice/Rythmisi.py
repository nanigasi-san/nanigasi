#被り防止でいきってギリシャ語つかおう
#ギリシャ語で「集合」らしい
'''
数字のみしか使えない
'''
import sympy as sp
x = sp.Symbol("x")
class Dimiourgia():#生成

    def olokliro(self,list_obj=[]):#全体集合の生成
        if isinstance(list_obj,list) == True:
            return sp.FiniteSet(*list_obj)

    def meros(self,oya,joukenn):#部分集合の生成
        emp1 = []
        for i in oya:
            ans = joukenn.subs(x,i)
            if ans == True:
                emp1.append(i)
        return sp.FiniteSet(*emp1)

    def sympliroma(self,zentai,bubun):#補集合の生成
        emp2 = []
        for element in zentai:
            if (element in bubun) == False:
                emp2.append(element)
        return sp.FiniteSet(*emp2)
