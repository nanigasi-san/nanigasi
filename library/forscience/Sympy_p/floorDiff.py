from sympy import*
x = Symbol('x')
y = Symbol('y')
try:
    limit = int(input("limit>>"))
except:
    limit = 10000
g = sympify(input("f>>"))

print("\n[f="+str(g)+"]\n\n<<LIMITED["+str(limit)+"]>>\n\n__start__")
counter = 0

while True:
    g = diff(g,x)
    counter += 1

    result = "["+str(counter)+"]"+str(expand(g))

    if factor(expand(g)) != expand(g):
        result += "\n = "+str(factor(expand(g)))

    if g != 0:
        if diff(g) == g:
            print(result+"\n"+"   .\n"*3+"[n]"+str(g)+"\n"+"   .\n"*3+"Endless")
            break

        else:
            print(result+"\n")
            if counter >= limit:
                print("="*64+"limit stop"+"="*64)
                break
            else:
                continue
    else:
        print(result+"\n__finish__")
        break
#list使って三角関数などの重複管理
