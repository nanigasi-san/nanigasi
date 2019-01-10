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

    def kai(self,set1,set2):#和集合の生成
        return set1.union(set2)

    def proion(self,set1,set2):#積集合の生成
        return set1.intersect(set2)



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

from inspect import currentframe

def name(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    return (', '.join(names.get(id(arg),'???') for arg in args))
