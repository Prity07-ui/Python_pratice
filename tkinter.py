#tkinter

import tkinter as tk

root = tk.Tk()

root.title("My App")
root.geometry("300x200")

label = tk.Label(root, text="Hello Python")
label.pack()

root.mainloop()