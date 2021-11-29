# 04-frame_added_to_main_F21.py
import tkinter as tk

mainwindow = tk.Tk()
mainwindow.config(bg='magenta')
mainwindow.geometry("300x400")

myFrameBob = tk.Frame(mainwindow, bg="green", width = 200, height = 300)
myFrameBob.pack()
# myFrameBob.pack(side="top", fill="both", expand=True)
# using place to make it smaller than window to see it
# myFrameBob.place(x=10, y=5, relwidth=0.9, relheight=0.9)

btn_1 = tk.Button(myFrameBob, bg='orange', text='button one')
# btn_1.pack()
btn_1.pack(padx=20, pady=30)

mainwindow.mainloop()
