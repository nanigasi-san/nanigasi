S = input()
ans = 0

if S == "keyence":
    ans = 1

else:
    for i in range(len(S)+1):
        for j in range(i+1,len(S)+1):
            S_ = list(S)
            del S_[i:j]
            re = "".join(S_)
            if re != "keyence":
                continue
            else:
                ans = 1
                break

if ans == 0:
    print("NO")
else:
    print("YES")

#AC
