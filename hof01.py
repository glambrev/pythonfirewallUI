from Tkinter import *
import Pmw
#Pmw -- Python MegaWidgets

import os,time
import tkMessageBox
from Dialog import Dialog
from FileDialog import LoadFileDialog, SaveFileDialog
from tkFileDialog import askopenfilename
root = Tk()

mainFrame=Frame(root)
mainFrame.pack(fill=BOTH,expand=YES)
root.option_readfile('optionDB')
root.title('HOF Config')
Pmw.initialise()


def help():
	print var.get()	

def aboutHof(self):
		tkMessageBox.showinfo("About", "About")

################################
def closeApp():
    if tkMessageBox.askokcancel("Quit", "Do you really wish to quit HOF Config?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", closeApp)

###### open MAN iptables ########
def man_open():
    from Tkinter import*
    newWin=Tk()
    myTextWidget = Text(newWin,borderwidth=2,font=('Verdana',10),bg='#ffffdd',height=50, width=85,wrap=WORD)
    scroll = Scrollbar(newWin, command=myTextWidget.yview)
    myTextWidget.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT,fill=Y,anchor=NW)
    myFile=file("/root/man_iptables") # get a file handle
    newWin.title('MAN Iptables')
    myText= myFile.read() # read the file to variable
    myFile.close() # close file handle
    myTextWidget.insert(0.0,myText) # insert the file's text into the text widget
    myTextWidget.pack(expand=1, fill=BOTH) # show the widget

######nat how-to###########
def nat_open():
    from Tkinter import*
    newWin=Tk()
    myTextWidget = Text(newWin,borderwidth=2,font=('Verdana',10),bg='#ffffdd',height=50, width=85,wrap=WORD)
    scroll = Scrollbar(newWin, command=myTextWidget.yview)
    myTextWidget.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT,fill=Y,anchor=NW)
    myFile=file("/root/nat-how") # get a file handle
    newWin.title('NAT How -To')
    myText= myFile.read() # read the file to variable
    myFile.close() # close file handle
    myTextWidget.insert(0.0,myText) # insert the file's text into the text widget
    myTextWidget.pack(expand=1, fill=BOTH) # show the widget

    
#### Log file open ######
def log_open():
    from Tkinter import*
    newWin=Tk()
    myTextWidget = Text(newWin,borderwidth=2,font=('Verdana',10),bg='#ffffdd',height=300, width=180,wrap=WORD)
    scroll = Scrollbar(newWin, command=myTextWidget.yview)
    myTextWidget.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT,fill=Y,anchor=NW)
    myFile=file("/var/log/messages") # get a file handle
    newWin.title('/var/log/messages')
    myText= myFile.read() # read the file to variable
    myFile.close() # close file handle
    myTextWidget.insert(0.0,myText) # insert the file's text into the text widget
    myTextWidget.pack(expand=1, fill=BOTH) # show the widget
#### start script open    
def start_open():
    from Tkinter import*
    newWin=Tk()
    myTextWidget = Text(newWin,borderwidth=2,font=('Verdana',10),bg='#ffffdd',height=50, width=100,wrap=WORD)
    scroll = Scrollbar(newWin, command=myTextWidget.yview)
    myTextWidget.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT,fill=Y,anchor=NW)
    myFile=file("/etc/network/if-up.d/block-iptables") # get a file handle
    newWin.title('Iptables Start-Up Script')
    myText= myFile.read() # read the file to variable
    myFile.close() # close file handle
    myTextWidget.insert(0.0,myText) # insert the file's text into the text widget
    myTextWidget.pack(expand=1, fill=BOTH) # show the widget



##############################################
def go():
	p = os.popen("ifconfig eth1 | grep 'inet addr:'| grep -v '127.0.0.1' |cut -d: -f2 | gawk '{ print $1}'", 'r')
	for l in p.xreadlines():
		t2.insert(END, '%s' % l.rstrip())
		
		t2.update_idletasks()
def go2():
	p = os.popen("ifconfig eth0 | grep 'inet addr:'| grep -v '127.0.0.1' |cut -d: -f2 | gawk '{ print $1}'", 'r')
	for l in p.xreadlines():
		t1.insert(END, '%s' % l.rstrip())
		t1.update_idletasks()

def go3():
	p = os.popen("./iplisting.sh", 'r')
	for l in p.xreadlines():
		st.insert(END, '%s' % l.rstrip())
		st.see(END)
		st.update_idletasks()		
##### block and enable firewall ######		
def block_hof():
	pipe_block = os.popen("./block-iptables", 'r')
def allow_hof():
	pipe_open = os.popen("./allow-iptables", 'r')
def minimal_hof():
	pipe_open = os.popen("./minimal-iptables", 'r')


def allow_http():
	pipe_open = os.popen("./allow-iptables", 'r')
def allow_ssh():
	pipe_open = os.popen("./allow-iptables", 'r')
def allow_ping():
	pipe_open = os.popen("./allow-iptables", 'r')	
############### Dialog Func #############################

def blockHof(w):
    dialog = Pmw.Dialog(root, buttons=('Apply', 'Cancel'),defaultbutton='Apply', title='Confirm Selection',command=block_hof())
    return  w

def about ():
    
    Pmw.aboutversion('1.0')
    Pmw.aboutcopyright('Copyright George Lambrev 2007\nAll rights reserved')
    Pmw.aboutcontact(
    '  IS2S52 - Project - IS (2006/07):\n' +
    '  George Lambrev\n' +
    '  Phone: 01446737808\n' +
    '  email: glambrev at gmail.com')
    about = Pmw.AboutDialog(root, applicationname='HOF')


def go4():
	p = os.popen("./iplisting.sh",'r')
	for l in p.xreadlines():
		t.insert(END, '%s\n' % l.rstrip())
		t.see(END)
		
		t.update_idletasks()
def clear():
    t.delete(1.0, END)


###############################################
balloon = Pmw.Balloon(mainFrame)
menubar = Pmw.MenuBar(mainFrame, hull_relief=RAISED,	hull_borderwidth=1,balloon=balloon)
menubar.pack(fill=X)

menubar.addmenu('File', 'File')

var = StringVar()
var.set('First')
menubar.addmenuitem('File', 'radiobutton', indicatoron=0,label='Open Log', command=log_open,
    value='o', variable=var)
menubar.addmenuitem('File', 'radiobutton', indicatoron=0,label ='if-up.d sh', command=start_open,
    value='s', variable=var)
#menubar.addmenuitem('File', 'radiobutton', indicatoron=0,label ='', command=help,
    #value='Third', variable=var)
menubar.addmenuitem('File', 'radiobutton', indicatoron=0,label ='Exit', command=closeApp,
    value='Fourth', variable=var)


menubar.addmenu('Help', 'Help',side='right')
menubar.addmenuitem('Help', 'radiobutton', indicatoron=0,label ='MAN Ipt..', command=man_open,
                    value='man', variable=var)
menubar.addmenuitem('Help', 'radiobutton', indicatoron=0,label ='NAT how..', command=nat-open,
                    value='abt', variable=var)
menubar.addmenuitem('Help', 'radiobutton', indicatoron=0,label ='About....', command=about,
                    value='abt', variable=var)
############http://floppsie.comp.glam.ac.uk/Glamorgan/gaius/scripting/16.html
todayIs= ' '
Date=Label(mainFrame, font=('verdana', 12),bg='gray85')
Date.pack(anchor=NE)
def data():
    global todayIs
    today=time.ctime(time.time())
    if today!= todayIs:
        todayIs=today
        Date.config(text=today)
data()

############ Main Frame ########
notebook = Pmw.NoteBook(mainFrame)
notebook.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

# Add the "Appearance" page to the notebook.
pageG = notebook.add('General Setup')





notebook.tab('General Setup').focus_set()

#######Radio Selection#########


group = Pmw.Group(pageG, tag_text = 'Activate Firewall')
group.pack(fill = 'both', expand = 1, padx = 10, pady = 10)



def call():
    variant = v.get()
    #variant= v.block_hof()
    print '"Option %s "' % variant
    if variant == 1:
        v.action= block_hof()
    elif variant == 2:
	action = allow_hof()	
    elif variant ==3:
        action = minimal_hof()
    else:
        pass

global v
v = IntVar()




radiobutton = Radiobutton(group.interior(),selectcolor='Orange',text= "Emergency Lockdown  ", variable=v, value="1")
radiobutton.pack()

radiobutton = Radiobutton(group.interior(),selectcolor='Orange',text= "Enable All Traffic  ", variable=v, value="2")
radiobutton.pack()

radiobutton = Radiobutton(group.interior(),selectcolor='Orange',text= "Minimal  Protection ", variable=v, value="3")
radiobutton.pack()

radiobutton.select()

gBut = Button(pageG,text=" Apply ",command=call)
gBut.pack(side=RIGHT)






#radioSel = Pmw.RadioSelect(group.interior(), labelpos=W,frame_borderwidth=1, frame_relief=FLAT,orient=VERTICAL,buttontype = 'radiobutton',command=blockHof)
#radioSel.pack(padx=10, pady=10)side=TOP,anchor=W




#for text in ('Disable Firewall', 'Enable Firewall', 'Emergency Lockdown'):
    #radioSel.add(text)
#horiz.invoke('Enable Firewall')

##################################################    

#fm2=Frame(root,width=300,height=100)

group = Pmw.Group(mainFrame, tag_text='Your IP Address')
group.pack(fill='both', expand=1, padx=6, pady=6)


t1 = Pmw.EntryField(group.interior(),value=' eth0  : ')

t1.pack(side=TOP)

Button(group.interior(), relief=GROOVE,bg='gray80',borderwidth=3,highlightbackground='gray80',text="Internet Interface", command=go2).pack(side=TOP)


t2 = Pmw.EntryField(group.interior(),value=' eth1  : ')

t2.pack(side=TOP)

Button(group.interior(), relief=GROOVE,borderwidth=3,bg='gray80',highlightbackground='gray80',text="Private Interface ", command=go).pack(side=TOP)


################  Filter Table ############################
pageF = notebook.add('Filter Table')

group = Pmw.Group(pageF, tag_text = 'Select Services')
group.pack(fill = 'both', expand = YES, padx = 10, pady = 10)


def fOpt():
    choice = fRull.get()
    
    print '"Option %s "' % variant
    if choice == 1:
        action= block_hof()
    elif variant ==2:
        action = allow_hof()
    else:
        pass

global fRull
fRull = IntVar()


radiobutton = Radiobutton(group.interior(),bg='gray80',text= "Internet Access", variable=v, value="4",selectcolor='Orange',activebackground='gray90')
radiobutton.pack(side=TOP)

radiobutton = Radiobutton(group.interior(),bg='gray80',text= "Enable SSH     ", variable=v, value="5",selectcolor='Orange',activebackground='gray90')
radiobutton.pack(side=TOP)

radiobutton = Radiobutton(group.interior(),bg='gray80',text= "Enable FTP     ", variable=v, value="6",selectcolor='Orange',activebackground='gray90')
radiobutton.pack(side=TOP)
radiobutton = Radiobutton(group.interior(),bg='gray80',text= "Enable DNS     ", variable=v, value="7",selectcolor='Orange',activebackground='gray90')
radiobutton.pack(side=TOP)

radiobutton.select()

fBut = Button(pageF,text=" Apply ")
fBut.pack(side=RIGHT)

################ Nat Table ##################

pageN = notebook.add('NAT Table')

group = Pmw.Group(pageN, tag_text = 'Network Address Translation')
group.pack(fill = 'both', expand = YES, padx = 10, pady = 10)

radiobutton = Radiobutton(group.interior(),bg='gray80',text= "Masquerade ", variable=v, value="1",selectcolor='Orange',activebackground='gray90')
radiobutton.pack()


radiobutton.select()

nBut = Button(pageN,text=" Apply ")
nBut.pack(side=RIGHT)

############# Show Rules  #########################
pageS = notebook.add('Rules')


group.pack(fill = 'both', expand = YES, padx = 10, pady = 10)

frameRules=Frame(pageS)
frameRules.pack()
t = Text(frameRules,borderwidth=2,font=('Verdana',10),bg='#ffffdd',height=16.3, width=75,wrap=WORD)
scroll = Scrollbar(frameRules, command=t.yview)
t.configure(yscrollcommand=scroll.set)

t.pack(side=LEFT,fill=X)
scroll.pack(side=RIGHT,fill=Y,anchor=NW)

showB = Button(pageS,text="  Show ",command=go4)
showB.pack(side=RIGHT)
showB = Button(pageS,text=" Clear ",command=clear)
showB.pack(side=RIGHT)
          
########### Show the Frame ####




root.geometry("600x600")
exitButton = Button(mainFrame, text = " Exit ", command = root.destroy)
exitButton.pack(side='right')


mainFrame.pack()
root.resizable(0,0)
root.mainloop()
