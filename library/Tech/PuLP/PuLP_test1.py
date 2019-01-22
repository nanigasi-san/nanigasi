#URL = https://qiita.com/mzmttks/items/82ea3a51e4dbea8fbc17

import pulp as lp #Linear Programming

#線形計画の定義
problem = lp.LpProblem("Curry_Oyako",lp.LpMaximize)

#変数の定義
Curry = lp.LpVariable("Curry",0,10,"Integer")
Oyako = lp.LpVariable("Oyako",0,10,"Integer")

#目的関数の定義
problem += 2*Curry + 3*Oyako

#制約関数の定義
problem += Curry + 2*Oyako <= 10
problem += 2*Curry + Oyako <= 8

#解く
status = problem.solve()
print(lp.LpStatus[status])

#結果表示
print("Result")
print("Curry:",Curry.value())
print("Oyako:",Oyako.value())
