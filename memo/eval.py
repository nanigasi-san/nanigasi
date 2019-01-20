import sympy as sp
x = sp.Symbol("x")
y = sp.Symbol("y")

def c(a):
    print(a,":",type(a))

def ato(siki):
    ex = eval(siki)
    return ex

expr1 = "x==4"
x = x.subs(x,4)
expr2 = (x == 4)
expr3 = ato(expr1)
expr4 = sp.sympify(expr1)
expr5 = eval(expr1)
c(expr1)
c(expr2)
c(expr3)
c(expr4)
c(expr5)
