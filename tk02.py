import tkinter as tk


win = tk.Tk()
win.title("我的窗口")
win.geometry("400x300")


ety1 = tk.Entry(win,show='*')
ety1.pack()

labVar = tk.StringVar()
lab = tk.Label(win,textvariable = labVar,bg="blue",font=("Arial",12),width=15,height=2)
lab.pack()

on_hit = False
def btn_click():
    global on_hit
    if on_hit == False:
        on_hit = True
        labVar.set("Hello TK")
    else:
        on_hit = False
        labVar.set("")

btn = tk.Button(win,text = "显示",width=15,height=2,command=btn_click)
btn.pack()

win.mainloop()

