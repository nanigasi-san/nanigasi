# In[]:
from sympy import Symbol, sympify, simplify


class Sequence():
    n = Symbol("n")
    first_term = 0
    general_term = 0

    def __init__(self, expr):
        self.general_term = sympify(expr)
    def get_term(self,n):
        return self.general_term.subs({"n":n})

    def enumeration(self, start, stop):
        return (self.get_term(i) for i in range(start, stop + 1))


class ArithmeticalProgression(Sequence):
    common_diff = 0

    def __init__(self, first_term, common_diff):
        self.first_term = first_term
        self.common_diff = common_diff
        self.general_term = sympify(self.first_term + (self.n - 1) * self.common_diff)


class GeometricProgression(Sequence):
    common_ratio = 0

    def __init__(self, first_term, common_ratio):
        self.first_term = first_term
        self.common_ratio = common_ratio
        self.general_term = sympify(self.first_term * self.common_ratio**(self.n - 1))

