with open("eng.txt","r",encoding="utf-8") as f1:
    eng_list = [eng.strip() for eng in f1.readlines()]
with open("jap.txt","r",encoding="utf-8") as f2:
    jpa_list = [jpa.strip() for jpa in f2.readlines()]

all = len(eng_list)
ok = 0
miss = 0
for eng,jpa in zip(eng_list,jpa_list):
    input_word = input(jpa+"\n"+"Hint：{0}".format(eng[:1]))
    if input_word in ["exit","puit"]:
        break
    if input_word == eng[1:]:
        print("OK!\n")
        ok += 1
    else:
        miss += 1
        print(eng)
        for i in range(5):
            input()

print("ok=>{0}(/{1}), miss=>{2}".format(ok,all,miss))
