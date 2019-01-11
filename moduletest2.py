from Alice import Rythmisi
dm = Rythmisi.Dimiourgia()

a = [1,2,3,4,5]
b = [3,4,5,6,7]
c = []
testa = dm.olokliro(a)
testb = dm.olokliro(b)
testc = dm.olokliro(c)

x = dm.kai(testa,testb,testc)
print(x)
