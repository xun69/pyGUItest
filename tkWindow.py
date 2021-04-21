import tkinter as tk

win = tk.Tk()
win.geometry("600x400+800+400")
win.title("tkWindow代码生成器")

# 标题
labTitle = tk.Label(win)
labTitle["text"] = "标题"
labTitle.place(x=10,y=10)

txtTitle = tk.Entry(win)
txtTitle.place(x=60,y=10)

# 宽度x高度
labWH = tk.Label(win)
labWH["text"] = "宽x高"
labWH.place(x=10,y=40)

txtW = tk.Entry(win)
txtW["width"] = 5 
txtW.place(x=60,y=40)

txtH = tk.Entry(win)
txtH["width"] = 5 
txtH.place(x=130,y=40)


win.mainloop()