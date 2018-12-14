from tkinter import Tk,Button,filedialog
from tkinter.scrolledtext import ScrolledText
import tkinter
import codecs

root = Tk()
root.geometry("500x400+400+200")
root.title("editer")

scrolledtext = ScrolledText(root,state='normal',font=("",12))
scrolledtext.place(x=20,y=20,width=480,height=340)

def save(self):
    name = filedialog.asksaveasfilename()
    text = scrolledtext.get("1.0",tkinter.END)

    f = codecs.open(name,"w","utf-8")
    f.write(text)
    f.close()

btn = Button(root,text="Save")
btn.place(x=20,y=370,width=80,height=20)
btn.bind("<ButtonRelease-1>",save)

btnex = Button(root)
btnex.config(text="Exit")
btnex.place(x=110,y=370,width=80,height=20)
btnex.bind("<Button-1>",exit)

root.mainloop()
