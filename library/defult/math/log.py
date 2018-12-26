import math
def type1():
    type = input("+ or -")
    t1 =int(input("底１"))
    s1 =int(input("真数１"))
    t2 = int(input("底２"))
    s2 = int(input("真数２"))

    left = math.log(s1,t1)
    right = math.log(s2,t2)
    if type == "+":
        answer = left + right
    elif type == "-":
        answer = left - right

    print(round(answer,5))
type1()
