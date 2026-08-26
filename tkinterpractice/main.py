# import tkinter as tk
# root=tk.Tk()
# root.title("Radiobutton attempt")
# root.geometry("300x200")
# a=tk.IntVar()
# a.set(2)
#
# def click(Value):
#     myLabel=tk.Label(root,text=Value)
#     myLabel.pack()
# radio1=tk.Radiobutton(root,text="Option 1",variable=a,value=1,command=click)
# radio2=tk.Radiobutton(root,text="Option 2",variable=a,value=2,command=click)
# radio1.pack()
# radio2.pack()
#
# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Radiobutton attempt")
root.geometry("300x200")

a = tk.IntVar()
a.set(2)

def click():
    myLabel = tk.Label(root, text=a.get())
    myLabel.pack()

radio1 = tk.Radiobutton(root, text="Option 1", variable=a, value=1, command=click)
radio2 = tk.Radiobutton(root, text="Option 2", variable=a, value=2, command=click)

radio1.pack()
radio2.pack()

root.mainloop()
