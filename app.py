from Tkinter import *
import createWikiPage as creator
import tkMessageBox

def createpage():
   	keyword=E1.get()
   	if not keyword:
		tkMessageBox.showinfo( "Sindhipedia", "No keyword provided")
   	else:	
		pageStatus['text']=creator.create_page(keyword);
		pageStatus['fg']="green"

def deletepage():
	keyword=E1.get()
	if not keyword:
		tkMessageBox.showinfo( "Sindhipedia", "No keyword provided")
	else:	
		pageStatus['text']=creator.delete_page(keyword);
		pageStatus['fg']="red"


root = Tk()
root.minsize(width=300, height=240)
root.maxsize(width=300, height=240)
root.resizable(width=False, height=False)
pageStatusLabel = Label(root, text="Status", fg="black")
pageStatusLabel.pack()
pageStatus = Label(root,text="Idle", fg="red")
pageStatus.pack()
connectStatusLabel = Label(root, text="Connection to Wiki", fg="black")
connectStatusLabel.pack()
connectStatus = Label(root,text="Not Connected", fg="red")
connectStatus.pack()
text = Text(root)
L1 = Label(root, text="Keyword")
L1.pack( side = LEFT)
E1 = Entry(root, bd =5)
E1.pack(side = LEFT)	
#if there is a searchword 
Bcreate = Button(root, text ="Create Page", command = createpage)
Bcreate.pack(anchor= SW,pady= 30)
Bdelete = Button(root, text ="Delete Page", command = deletepage)
Bdelete.pack(anchor = SW)
if(creator.init_connection()== 0):
	connectStatus['text']= "Could Not Connect";
	connectStatus['fg']= "red"
else:
	connectStatus['text']= "Connection Established"
	connectStatus['fg']= "green"	
root.mainloop()