from tkinter import Tk,Button

root = Tk()
btn = Button(root)
btn.config(text="EXIT")
btn.place(x=5,y=5,width=100,height=50)
btn.bind("<Button-1>",exit)
root.mainloop()
#<Button-1>; 左クリック
#<Button-2>; ホイールクリック
#<Button-3>; 右クリック
