import os
from Tkinter import *
import Pmw

root = Tk()
t = Text(root)

t.pack(side=TOP)

def go():
	p = os.popen("./block-iptables", 'r')
	for l in p.xreadlines():
		t.insert(END, '%s\n' % l.rstrip())
		#t.see(END)
		t.update_idletasks()

Button(root, text='Go', command=go).pack(side=TOP)
root.geometry("600x500")
root.mainloop()

