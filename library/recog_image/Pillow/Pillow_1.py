from PIL import Image
src = Image.open("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/str.jpg")
dest = src.rotate(45) #45°回転
dest.save("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/dest.png","PNG")

dest2 = src.resize((100,100))
dest2.save("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/dest2.png","PNG")

dest3 = src.quantize(3)
dest3.save("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/dest3.png","PNG")

hist = src.histogram()
print(hist)

print(src.getpixel((10,10)))
src.putpixel((10,10),(1,2,3))
print(src.getpixel((10,10)))

from PIL import ImageFilter
dest4 = src.filter(ImageFilter.BLUR)
dest4.save("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/dest4.png","PNG")

dest5 = src.filter(ImageFilter.CONTOUR)
dest5.save("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/dest5.png","PNG")

dest6 = src.filter(ImageFilter.DETAIL)
dest6.save("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/dest6.png","PNG")

dest7 = src.filter(ImageFilter.EDGE_ENHANCE)
dest7.save("C:/Users/Username/Documents/GitHub/nanigasi/library/recog_image/Pillow/image/dest7.png","PNG")
