#被り防止でいきってギリシャ語つかおう
#ギリシャ語で「集合」らしい
'''
数字のみしか使えない
'''

import sympy as sp

class Dimiourgia():#生成
    x = sp.Symbol("x")

    def olokliro(self,object=[]):#(全体)集合の生成
        return sp.FiniteSet(*object)

    def meros(self,super,constraint):#部分集合の生成
        emp = []
        x = self.x
        for i in super:
            x = x.subs(x,i)
            expr = eval(constraint)
            if expr == True:
                emp.append(i)
        return sp.FiniteSet(*emp)

    def sympliroma(self,super,sub):#補集合の生成
        emp2 = []
        for element in super:
            if (element in sub) == False:
                emp2.append(element)
        return sp.FiniteSet(*emp2)

    def kai(self,*args):#和集合の生成
        kai = sp.FiniteSet()
        for element in args:
            kai = kai.union(element)
        return kai

    def proion(self,*args):#積集合の生成
        proion = args[0]
        for element in args:
            proion = proion.intersect(element)
        return proion

    def ekthetiki(self,set):#冪集合の生成
        return set.powerset()
