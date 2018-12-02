N = int(input())
counter = 0
list = ['1','2','4','5','6','8','9']
for i in range(N+1):
    if '3' in str(i):
        if '5' in str(i):
            if '7' in str(i):
                for _ in list:
                    if _ not in str(i):
                        continue
                    else:
                        break
                counter += 1
print(counter)
