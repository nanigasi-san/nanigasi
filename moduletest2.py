from Alice import Rythmisi
import sympy as sp
dm = Rythmisi.Dimiourgia()

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8,10,12,14,16,18,20]

test1 = dm.olokliro(list1)
test2 = dm.olokliro(list2)

print(test1,test2)

x = dm.x
expr = (x==3)
test3 = dm.meros(test1,sp.sympify(expr))
print(test3)
