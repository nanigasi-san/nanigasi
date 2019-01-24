from Alice import Rythmisi

dm = Rythmisi.Dimiourgia()

x = dm.x
list=[1,2,3,4,5,6,7,8,9,10]
sublist = [2,4,6,8,10,12,14,16,18,20]

sub = dm.olokliro(sublist)

test1 = dm.olokliro(list)
print("生成",test1)

a = sub+test1
print(a) 
