import tkinter
import re

root = tkinter.Tk()

try:
    fh = open('/usr/share/dict/words')
    words = list(map(lambda x: x[:-1] if x[-1] == '\n' else x, \
            fh.readlines()))
    fh.close()
except:
    print('cannot open file')
    root.destroy()

def apply_reg_expr():
    regexp = pat_str.get()
    if len(regexp) == 0:
        return 
    matched_words = [w for w in words if re.search(regexp, w)]
    result_box.delete(0, tkinter.END)
    for i, w in enumerate(matched_words):
        result_box.insert(i, w)

f = tkinter.Frame(root, borderwidth = 5)
pat_str = tkinter.StringVar()

pat_label = tkinter.Label(f, text = 'Pattern', justify = tkinter.RIGHT)
pat_entry = tkinter.Entry(f, textvariable = pat_str)
find_btn = tkinter.Button(f, text = 'find', command = apply_reg_expr)
result_box = tkinter.Listbox(f)

f.grid(row = 0, column = 0)
pat_label.grid(row = 0, column = 0)
pat_entry.grid(row = 0, column = 1)
find_btn.grid(row = 0, column = 2)
result_box.grid(row = 1, column = 0, columnspan = 3)

f.mainloop()
