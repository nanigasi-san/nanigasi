import sys

while True:
    responce = input("終了するにはexitと入力してください。")
    if responce == "exit":
        sys.exit()
    print(responce + "と入力されました。")
