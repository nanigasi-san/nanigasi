# In[]:
from sympy import Symbol, sympify, simplify


class Sequence():
    n = Symbol("n")
    first_term = None
    general_term = None

    def __init__(self, expr):
        self.general_term = sympify(expr)

    def get_term(self,num):
        return self.general_term.subs({"n":num})

    def enumeration(self, start, stop):
        return (self.get_term(i) for i in range(start, stop + 1))



class ArithmeticalProgression(Sequence):
    common_diff = None

    def __init__(self, first_term, common_diff):
        self.first_term = first_term
        self.common_diff = common_diff
        self.general_term = sympify(self.first_term + (self.n - 1) * self.common_diff)


class GeometricProgression(Sequence):
    common_ratio = None

    def __init__(self, first_term, common_ratio):
        self.first_term = first_term
        self.common_ratio = common_ratio
        self.general_term = sympify(self.first_term * self.common_ratio**(self.n - 1))

class Zennka1(Sequence):
    a_n = Symbol("a_n")
    recurrence_fomula = None # `a_n+1 = `の式の右辺
    def __init__(self,first_term,recurrence_fomula):
        self.first_term = first_term
        self.recurrence_fomula = sympify(recurrence_fomula)
    def zenka(self,stop):
        zenka_list = [self.first_term]
        for _ in range(2,stop+1):
            zenka_list.append(self.recurrence_fomula.subs({"a_n":zenka_list[_-2],"n":_-1}))
        return zenka_list
