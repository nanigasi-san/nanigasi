import requests
URL = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
res = requests.get(URL).text
with open("face.xml","w") as f:
    f.write(res)