import tkinter as tk #引入Tkinter

# 根节点
root_win = tk.Tk() 
root_win.title("我的窗口")
root_win.geometry("600x400")


main_frm = tk.Frame(
    root_win,
    width=100,
    height=100
)

left_frm = tk.Frame(
    main_frm,
    bg="red",
    width=100,
    height=100
).pack(side=tk.LEFT)

right_frm = tk.Frame(
    main_frm,
    bg="blue",
    width=100,
    height=100
).pack(side=tk.RIGHT)



lab1 = tk.Label(
    root_win,
    text="lab1",
    width=10,
    height=2,
    padx = 2,
    pady = 3
).pack()

btn = tk.Button(
    root_win,
    text="123",
    width=10,
    height=2
).pack()

main_frm.pack()

root_win.mainloop() # 进入窗体循环
