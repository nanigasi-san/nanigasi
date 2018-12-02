N = int(input())
counter = 0
list = ['3','5','7']
ok = []
for a in list:
    for b in list:
        for c in list:
            ok.append(a+b+c)
            for d in list:
                ok.append(a+b+c+d)
                for e in list:
                    ok.append(a+b+c+d+e)
                    for f in list:
                        ok.append(a+b+c+d+e+f)
                        for g in list:
                            ok.append(a+b+c+d+e+f+g)
                            for h in list:
                                ok.append(a+b+c+d+e+f+g+h)
                                for i in list:
                                    ok.append(a+b+c+d+e+f+g+h+i)
                                    for j in list:
                                        ok.append(a+b+c+d+e+f+g+h+i+j)

okk = []
for _ in ok:
    x3 = _.count('3')
    x5 = _.count('5')
    x7 = _.count('7')
    if x3>0 and x5>0 and x7>0:
        okk.append(_)
fin = [int(_) for _ in okk]
fin.sort()
for _ in fin:
    if _ > N:
        print(fin.index(_))
        break
