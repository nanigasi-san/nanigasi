from tkinter import Tk,Label,Entry,Checkbutton,Scale
from tkinter.scrolledtext import ScrolledText
import tkinter

root = Tk()
root.geometry("500x400+10+10")
label = Label(root,text="label")
label.place(x=5,y=5,width=100,height=30)
#==========================================================
from PIL import Image,ImageTk

#image = ImageTk.PhotoImage(Image.open("imagefile/image.png"))   \
#glabel = Label(root,image=image                                 -> 動かない
#glabel.place(x=5,y=50,width=100,height=100)                     /

entry = Entry(root)
entry.place(x=5,y=160,width=100,height=30)
entry.insert(tkinter.END,"entry")
print("entry=" + entry.get())

bv = tkinter.BooleanVar()
bv.set(True)
checkbtn = Checkbutton(root,text="checkbutton",variable=bv)
checkbtn.place(x=5,y=205,width=100,height=30)

print("checkbtn=" + str(bv.get()))

scale = Scale(root,orient="horizontal")
scale.place(x=205,y=5,width=100,height=50)
scale.set(30)
print(scale.get())

scrolledtext = ScrolledText(root,state="normal")
scrolledtext.place(x=205,y=75,width=200,height=100)

scrolledtext.insert(tkinter.END,"scrolled text")
print(scrolledtext.get("1.0","1.2"))

root.mainloop()
