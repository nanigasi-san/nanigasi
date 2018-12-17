from PIL import Image
img = Image.new('RGBA',(500,500),(255,255,255,0))

from PIL import ImageDraw
draw = ImageDraw.Draw(img)

draw.line((100,100,100,500),fill=(80,0,0),width=10)
img.save("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/out.png")

draw.rectangle((110,100,410,300),outline=(0,0,0))
img.save("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/out.png")

draw.ellipse((195,140,315,260),fill=(190,0,63))
img.save("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/out.png")
