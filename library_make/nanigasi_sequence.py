# In[]:
from sympy import Symbol, sympify, simplify


class Sequence():
    n = Symbol("n")
    first_term = None #継承用変数
    general_term = None

    def __init__(self, general_term):
        self.general_term = sympify(general_term)

    def get_term(self,num):
        return self.general_term.subs({"n":num})

    def enumeration(self, start, end):
        return (self.get_term(i) for i in range(start, end + 1))
    
    def sigma(self,start,end):
        return sum(self.enumeration(start,end))


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

    def enumeration(self,start,end):
        num_log = None #前世の記憶
        _ = 1
        while _ < start:
            if _ == 1:
                num_log = self.first_term
            else:
                num_log = self.recurrence_fomula.subs({"a_n":num_log,"n":_})
            _ += 1
        for _ in range(start,end+1):
            if _ == 1:
                num_log = self.first_term
            else:
                num_log = self.recurrence_fomula.subs({"a_n":num_log,"n":_})
            yield num_log


class Zennka2(Sequence):
    a_n = Symbol("a_n")
    a_n_plus1 = Symbol("a_n_plus1")
    second_term = None
    recurrence_fomula = None # `a_n+2 = `の式の右辺
    def __init__(self,first_term,second_term,recurrence_fomula):
        self.first_term = first_term
        self.second_term = second_term
        self.recurrence_fomula = sympify(recurrence_fomula)

    def enumeration(self,start,end):
        _ = 1
        while True:
            if _ == 1:
                num_log1 = self.first_term
                num_log2 = self.second_term
                _ += 1
                if start == 1:
                    yield num_log1
            else:
                num_log1,num_log2 = num_log2,self.recurrence_fomula.subs({"a_n":num_log1,"a_n_plus1":num_log2,"n":_})
                _ += 1
            if start <= _ <= end:
                yield num_log2
            if _ > end:
                break