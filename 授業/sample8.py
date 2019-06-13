import time
nasu = 0
while True:
    while nasu < 65:
        nasu += 1
        print("🍆"*nasu)
        time.sleep(0.1)
    while nasu > 1:
        nasu -= 1
        print("🍆"*nasu)
        time.sleep(0.1)