import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("400x600+100+100")

# "添加新按钮"单击事件
def add_btn_click():
    n_btn = tk.Button(
        root,
        text="添加新按钮",
        width=100,
        height=10
    ).pack()



tvw1 = ttk.Treeview(
    root,
    height=100
).pack(side=tk.LEFT,fill="both")

itm = ttk.Treeview.item(
    tvw1,
    tvw1,
    text="123"
).pack()

add_btn = tk.Button(
    root,
    text="添加新按钮",
    width=100,
    height=10,
    command = add_btn_click
).pack()

root.mainloop()