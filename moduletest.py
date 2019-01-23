from Alice import Rythmisi

dm = Rythmisi.Dimiourgia()

x = dm.x
list=[1,2,3,4,5,6,7,8,9,10,50,100,1000,9999,1/3,3.14]
sublist = [2,4,6,8,10,100]

sub = dm.olokliro(sublist)

test1 = dm.olokliro(list)
print("生成",test1)

test2 = dm.meros(test1,"x%2==0")
print("部分",test2)

test3 = dm.sympliroma(test1,test2)
print("補",test3)

test4 = dm.athroisma(test1,sub)
print("和",test4)

test5 = dm.proion(test1,sub)
print("積",test5)

test6 = dm.diafora(test1,sub,test3)
print("差",test6)

test7 = dm.ekthetiki(sub)
print("冪",test7)
