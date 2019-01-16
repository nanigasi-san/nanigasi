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
        emp1 = []
        for i in super:
            ans = constraint.subs(self.x,i)
            if ans == True:
                emp1.append(i)
        return sp.FiniteSet(*emp1)

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

class Krisi():#判別
    def einai_meros(self,ask_super,ask_sub):#「である」
        return ask_super.is_superset(ask_sub)

class Axia():#値
    pass
