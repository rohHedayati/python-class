import tkinter as tk
from tkinter import ttk

def event():
    print("Hi")


root = tk.Tk(className="My App")
root.geometry('600x400+150+50')
# root.resizable(False, False)
photo = tk.PhotoImage(file='./download.png', width=50, height=50)
# root.iconphoto(False, photo)

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

name_var = tk.StringVar()
name_entry = ttk.Entry(root, textvariable=name_var)
name_entry.pack()
name_entry.focus()


output_label = ttk.Label(root)
output_label.pack()

name_var.trace_add(
    "write", 
    lambda *args: output_label.config(text=name_var.get().upper())
)
ttk.Button(root, text="Click", command=event, image=photo, compound=tk.LEFT).pack(ipadx=10, ipady=10)

root.mainloop()