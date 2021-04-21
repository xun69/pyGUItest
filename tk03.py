import tkinter as tk

root_win = tk.Tk()
root_win.title("123")
root_win.geometry("500x600")

txt1 = tk.Text(
    root_win,
    width =100,
    height = 10
).place(x=20,y=20,anchor="nw")

root_win.mainloop()