import tkinter as tk

win = tk.Tk()
win.geometry("600x400+800+400")
win.title("tkWindow代码生成器")


# 申明字符变量
title_var = tk.StringVar()
w_var = tk.StringVar()
h_var = tk.StringVar()
top_var = tk.StringVar()
left_var = tk.StringVar()

code_var = tk.StringVar()


# 标题
labTitle = tk.Label(win)
labTitle["text"] = "标题"
labTitle.place(x=10,y=10)

txtTitle = tk.Entry(win,textvariable = title_var)
txtTitle.insert(0,"我的窗体") # 默认窗体名称
txtTitle.place(x=60,y=10)

# 宽度x高度
labWH = tk.Label(win)
labWH["text"] = "宽x高"
labWH.place(x=10,y=40)

txtW = tk.Entry(win,textvariable = w_var)
txtW["width"] = 5 
txtW.insert(0,"400") #默认窗体宽度
txtW.place(x=60,y=40)

txtH = tk.Entry(win,textvariable = h_var)
txtH["width"] = 5 
txtH.insert(0,"300") #默认窗体高度
txtH.place(x=130,y=40)

# +top+left
labTL = tk.Label(win)
labTL["text"] = "顶+左"
labTL.place(x=170,y=40)

txtLeft = tk.Entry(win,textvariable = left_var)
txtLeft["width"] = 5 
txtLeft.insert(0,"600") #默认窗体Left值
txtLeft.place(x=260,y=40)

txtTop = tk.Entry(win,textvariable = top_var)
txtTop["width"] = 5 
txtTop.insert(0,"400") #默认窗体Top值
txtTop.place(x=330,y=40)

has_Run = False #是否已经有一个窗体实例运行
# 运行窗体实例
def run_Window():
    global new_win
    global title_var
    global h_var
    global w_var
    global top_var
    global left_var

    global code_var
    global has_Run

    if has_Run == False:
        new_win = tk.Tk()
        new_win.geometry(w_var.get() + "x" + h_var.get()  + "+" + left_var.get() + "+" + top_var.get())
        new_win.title(title_var.get()) 

        # 生成代码并显示
        code_str = "import tkinter as tk\n\n"
        code_str += "win = tk.Tk()\n"
        code_str += "win.geometry('" + w_var.get() + "x" + h_var.get() + "+" + left_var.get() + "+" + top_var.get() + "')\n"
        code_str += "win.title('" + title_var.get() + "')\n\n"
        code_str += "win.mainloop()\n"

        codeText.delete(1.0,"end")
        codeText.insert("insert",code_str)
        
        has_Run = True
        new_win.mainloop()
        
    else:
        has_Run = False
        new_win.destroy()
        run_Window() # 自己调用自己是否可行？没有Goto啊

# 运行按钮
btnRun = tk.Button(win)
btnRun["text"] = "运行"
btnRun["width"] = 10
btnRun["height"] = 1

btnRun["command"] = run_Window
btnRun.place(x=220,y=10)

def close_Window():
    new_win.destroy()

# 停止按钮
btnRun = tk.Button(win)
btnRun["text"] = "停止"
btnRun["width"] = 10
btnRun["height"] = 1

btnRun["command"] = close_Window
btnRun.place(x=300,y=10)



# 代码区
codeText =tk.Text(win)
codeText["width"]=44
codeText["height"]=11
codeText["font"]=('微软雅黑','16','bold')
codeText.place(x=10,y=80)



win.mainloop()