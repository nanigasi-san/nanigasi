from Alice import Rythmisi
dm = Rythmisi.Dimiourgia()
kr = Rythmisi.Krisi()

x = dm.x
list=[23,23.0,52,23,3.14,245/23,25,672,235,23]
list2 = [1,2,3,4,5]

sub = dm.olokliro(list2)
test1 = dm.olokliro(list)
print(test1)

test2 = dm.meros(test1,x<100)
print(test2)

test3 = dm.sympliroma(test1,test2)
print(test3)

test4 = dm.kai(test2,test3)
print(test4)

test5 = dm.proion(test1,test2)
print(test5)

kr.Syschetisi(test1,test2)
kr.Syschetisi(test1,test3)
kr.Syschetisi(test2,test1)
kr.Syschetisi(test2,test3)
kr.Syschetisi(test3,test1)
kr.Syschetisi(test3,test2)
