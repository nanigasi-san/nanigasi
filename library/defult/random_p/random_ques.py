import random
import time
import sys

sys.path.append("library/defult/random_p/score")

question_number = 1
number = 100
ok = 0
t_0 = time.time()
for i in range(question_number):
    a = random.randint(-number,number)
    b = random.randint(-number,number)
    if b<0:
        answer = int(input("{0}{1}=?".format(a,b)))
    else:
        answer = int(input("{0}+{1}=?".format(a,b)))
    if answer == a+b:
        ok += 1
t_1 = time.time()
miss = question_number-ok


point = ok*10
time = t_1-t_0
score = int((point/(time+miss))*1000)

f = open("library/defult/random_p/score/score.txt","r")
high_score = int(f.read())

print("POINT:{0}".format(point))
print("TIME:{0}s + {1}s(miss)".format(round(time,2),miss))
print("SCORE:{0}".format(score),end=" ")
if score>high_score:
    print("<<HIGH SCORE!!>>")
    f.close()
    f = open("library/defult/random_p/score/score.txt","w")
    f.write(str(score))
    f.close()
