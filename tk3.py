import tkinter

root = tkinter.Tk()
f = tkinter.Frame(root, width = 200, height = 150)
f.pack_propagate(0)
f.pack()

import datetime
today = datetime.date.today()
import calendar
cal = calendar.TextCalendar(6)
calstr = cal.formatmonth(today.year, today.month)

l = tkinter.Label(f, text = calstr, justify = tkinter.LEFT, font = ('Courier', 12))
l.pack(side = tkinter.TOP)

b = tkinter.Button(f, text = 'Quit', command = root.destroy)
b.pack(side = tkinter.BOTTOM)

tkinter.mainloop()
