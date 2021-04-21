import tkinter as tk
import os

win = tk.Tk()
win.geometry('400x300+600+400')
win.title('在.py中运行CMD的start命令打开网站')


def btnRun_click():
    os.system("start https://www.baidu.com/") # 打开网站

# 运行按钮
btnRun = tk.Button(win)
btnRun["text"] = "打开百度"
btnRun["width"] = 30
btnRun["height"] = 3
btnRun["command"] = btnRun_click
btnRun.place(x=10,y=10)



win.mainloop()