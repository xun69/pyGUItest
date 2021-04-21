import tkinter as tk
import os

win = tk.Tk()
win.geometry('400x300+600+400')
win.title('在.py中运行其他.py脚本文件')


def btnRun_click():
    os.system("python tkWindow.py") # 运行另一个python脚本文件

# 运行按钮
btnRun = tk.Button(win)
btnRun["text"] = "运行tkWindow.py"
btnRun["width"] = 30
btnRun["height"] = 3
btnRun["command"] = btnRun_click
btnRun.place(x=10,y=10)



win.mainloop()