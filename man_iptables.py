from Tkinter import *
import Pmw

root = Tk()
root.option_readfile('optionDB')
root.title('ScrolledText')
Pmw.initialise()

st = Pmw.ScrolledText(root, borderframe=1, labelpos=NW,
		label_text='Man Iptables', usehullsize=1,
		hull_width=800, hull_height=500,
		text_padx=10, text_pady=10,
		text_wrap='none')

st.importfile('man_iptables')
st.pack(fill=BOTH, expand=1, padx=5, pady=5)


root.mainloop()

