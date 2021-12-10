import time
from tkinter import *
from tkinter.messagebox import *
def fenetre(question, title, rep1, rep2, ret1, ret2):
	def Verif():
		if rep.get()==rep1:
			showinfo(title, ret1)
			Mafenetre.destroy()
		elif rep.get()==rep2:
			showinfo(title, ret2)
			Mafenetre.destroy()
		else:
			showwarning('attention','error')
			rep.set('')
	Mafenetre=Tk()
	Mafenetre.title(title)
	Label1=Label(Mafenetre, text= question)
	Label1.pack(side=LEFT, padx=5,pady=5)
	rep=StringVar()
	Champ=Entry(Mafenetre, textvariable=rep, bg='bisque', fg='maroon')
	Champ.focus_set()
	Champ.pack(side=LEFT, padx=5, pady=5)
	Bouton=Button(Mafenetre, text='valider',command=Verif)
	Bouton.pack(side=LEFT, padx=5, pady=5)
	Mafenetre.mainloop()

montemps=time.time()
y=time.time()-montemps
while time.localtime(y)[3]-1<1:
    y=time.time()-montemps
    time.sleep(1)
    print (time.localtime(y)[3]-1,'h',time.localtime(y)[4],'min',time.localtime(y)[5],'s')
    if (time.localtime(y)[4]%5)==0:
    	fenetre('un indice?', 'indice', 'oui', 'non', 'des friandises pour le chien sont\n posées dans une boite métalique sur \n le bureau','ok' )
print('fin')