def chk(obj):
    print(obj,type(obj))

from Alice import Rythmisi
import sympy as sp
dm = Rythmisi.Dimiourgia()
kr = Rythmisi.Krisi()
test1 = [1,2,3,4,5]
test2 = [1,2,3]

set1 = dm.olokliro(test1)
set2 = dm.olokliro(test2)
chk(set1)
chk(set2)
a = kr.einai_meros(set1,set2)
print(a)
