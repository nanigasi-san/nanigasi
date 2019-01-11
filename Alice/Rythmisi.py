#被り防止でいきってギリシャ語つかおう
#ギリシャ語で「集合」らしい
'''
数字のみしか使えない
'''

import sympy as sp

class Dimiourgia():#生成
    x = sp.Symbol("x")

    def olokliro(self,object=[]):#全体集合の生成
        return sp.FiniteSet(*object)

    def meros(self,oya,joukenn):#部分集合の生成
        emp1 = []
        for i in oya:
            ans = joukenn.subs(self.x,i)
            if ans == True:
                emp1.append(i)
        return sp.FiniteSet(*emp1)

    def sympliroma(self,zentai,bubun):#補集合の生成
        emp2 = []
        for element in zentai:
            if (element in bubun) == False:
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
    def Syschetisi(self,A,B):#相関の判別
        A_name,B_name = "Right","Left"
        if A == B:#同一
            print("{0}=={1}.".format(A_name,B_name))

        elif A != B:
            if len(A) != len(B):#濃度が違う
                if len(A) > len(B):
                    large = A
                    small = B
                    flg = "a"
                elif len(B) > len(A):
                    large = B
                    small = A
                    flg = "b"
                for element in small:
                    if (element in large) == True:
                        pass
                    else:
                        print("There is no correlation between {0} and {1}.".format(A_name,B_name))
                        break
                else:
                    if flg == "a":
                        print("{0} is a subset of {1}.".format(A_name,B_name))
                    else:
                        print("{0} is a subset of {1}.".format(B_name,A_name))

            else:
                print("There is no correlation between {0} and {1}.".format(A_name,B_name))
    def einai_(self):#「である」
        pass

class Axia():#値
    pass
