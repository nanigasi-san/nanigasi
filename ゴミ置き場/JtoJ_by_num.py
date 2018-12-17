def J_to_num_str(str):
    japaneselist = [["あ","い"],["か","き"],["さ","し"]]
    for a in range(len(japaneselist)):
        b = japaneselist[a]
        try:
            now = []
            now.append(a)
            now.append(b.index(str))
        except:
            continue
        if now != []:
            return now

def J_to_num_input():
    all = []
    injapa = list(input())
    for japa in injapa:
        all.append(J_to_num_str(japa))
    print(all)
    return all

def num_to_J(list):
    try:
        japaneselist = [["あ","い"],["か","き"],["さ","し"]]
        ans = []
        for _ in range(len(list)):
            a = list[_][0]
            b = list[_][1]
            ans.append(japaneselist[a][b])
        print("".join(ans))
    except:
        print("ERROR")

num_to_J(J_to_num_input())
