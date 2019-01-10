from Alice import Rythmisi
x = Rythmisi.x
dm = Rythmisi.Dimiourgia()
kr = Rythmisi.Krisi()


list=[23,23.0,52,23,3.14,245/23,25,672,235,23]

test1 = dm.olokliro(list)
print(test1)

test2 = dm.meros(test1,x<100)
print(test2)

test3 = dm.sympliroma(test1,test2)
print(test3)

kr.Syschetisi(test1,test2)
kr.Syschetisi(test1,test3)
kr.Syschetisi(test2,test1)
kr.Syschetisi(test2,test3)
kr.Syschetisi(test3,test1)
kr.Syschetisi(test3,test2)
