import tkinter
root = tkinter.Tk()

f = tkinter.Frame(root)
f.pack()

l = tkinter.Label(f, text = 'Hello World')
l.pack()

b = tkinter.Button(f, text = 'Quit', command = root.destroy)
b.pack()

tkinter.mainloop()
