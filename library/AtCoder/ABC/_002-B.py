W =  list(input())
No = ["a","i","u","e","o"]
list = []
for w in W:
    counter = 0
    for no in No:
        if w == no:
            break
        counter += 1
        if counter == 5:
            list.append(w)
print("".join(list))
#go
