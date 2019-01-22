import math as m

print("\n\n<<information>>")
print("Type1>>二項・係数なし")
print("Type2>>三項・係数なし")
print("Type3>>二項・係数あり")

def Type1():
    type = input("+ or -")
    t1 =int(input("底１"))
    s1 =int(input("真数１"))
    t2 = int(input("底２"))
    s2 = int(input("真数２"))

    left = m.log(s1,t1)
    right = m.log(s2,t2)
    if type == "+":
        answer = left + right
    elif type == "-":
        answer = left - right

    print(round(answer,5))


def Type2():
    type_first = input("first>> + or -")
    type_second = input("second>> + or -")

    t1 = int(input("底１"))
    s1 = int(input("真数１"))
    t2 = int(input("底２"))
    s2 = int(input("真数２"))
    t3 = int(input("底３"))
    s3 = int(input("真数３"))

    left = m.log(s1,t1)
    midium = m.log(s2,t2)
    right = m.log(s3,t3)

    if type_first == "+":
        if type_second == "+":
            answer = left+midium+right
        elif type_second == "-":
            answer = left+midium-right
    elif type_first == "-":
        if type_second == "+":
            answer = left-midium+right
        elif type_second == "-":
            answer = left-midium-right

    print(round(answer,5))
