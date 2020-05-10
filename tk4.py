import tkinter

root = tkinter.Tk()
f = tkinter.Frame(root, width = 250, height = 200)
f.pack_propagate(0)
f.pack()

import datetime
today = datetime.date.today()
current_year, current_month = today.year, today.month
import calendar
cal = calendar.TextCalendar(6)

calstr = tkinter.StringVar()
calstr.set(cal.formatmonth(today.year, today.month))

l = tkinter.Label(f, textvariable = calstr, justify = tkinter.LEFT, font = ('Courier', 12))
l.pack(side = tkinter.TOP)

b = tkinter.Button(f, text = 'Quit', command = root.destroy)
b.pack(side = tkinter.BOTTOM)

def prev_month():
    global current_year, current_month
    current_month -= 1
    if current_month == 0:
        current_month = 12
        current_year -= 1
    calstr.set(cal.formatmonth(current_year, current_month))

def next_month():
    global current_year, current_month
    current_month += 1
    if current_month == 13:
        current_month = 1
        current_year += 1
    calstr.set(cal.formatmonth(current_year, current_month))

pm = tkinter.Button(f, text = 'Prev', command = prev_month)
pm.pack(side = tkinter.LEFT)

nm = tkinter.Button(f, text = 'Next', command = next_month)
nm.pack(side = tkinter.RIGHT)

tkinter.mainloop()
