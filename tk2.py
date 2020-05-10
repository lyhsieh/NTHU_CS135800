import tkinter
root = tkinter.Tk()

f = tkinter.Frame(root, width = 200, height = 150)
f.pack_propagate(0)     #don't shrink
f.pack()

l = tkinter.Label(f, text = 'Hello World')
l.pack(side = tkinter.TOP)

b = tkinter.Button(f, text = 'Quit', command = root.destroy)
b.pack(side = tkinter.BOTTOM)

tkinter.mainloop()
