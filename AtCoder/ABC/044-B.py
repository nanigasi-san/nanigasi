w = list(input())
counter = 0
for _ in w:
    if w.count(_)%2 == 0:
        counter += 1
    else:
        print("No")
        break
    if counter == len(w):
        print("Yes")
#AC
