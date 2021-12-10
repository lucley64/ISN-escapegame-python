import time
from tkinter import *
from tkinter.messagebox import *
montemps=time.time()
y=0
def Verification():
    if indice.get()=='oui' or indice.get()=='non' or indice.get()=='o' or indice.get()=='n':
        if indice.get()=='oui' or indice.get()=='o':
            showinfo('des friandises pour le chien sont posées dans une boite métalique sur le bureau')
            Mafenetre.destroy()
        else: 
            showwarning('Répondez oui ou non')
            indice.set('')
while(time.localtime(y)[3]-1<1):
    y=time.time()-montemps
    time.sleep(1)
    print (time.localtime(y)[3]-1,'h',time.localtime(y)[4],'min',time.localtime(y)[5],'s')
    if time.localtime(y)[5]%10==0 and time.localtime(y)[5]>0:
        Mafenetre = Tk()
        Mafenetre.title('indice')
        Label1 = Label(Mafenetre, text = 'Besoin d un indice? ')
        Label1.pack(side = LEFT, padx = 5, pady = 5)
        indice= StringVar()
        Champ = Entry(Mafenetre, textvariable= indice, bg ='bisque', fg='maroon')
        Champ.focus_set()
        Champ.pack(side = LEFT, padx = 5, pady = 5)
        Bouton = Button(Mafenetre, text ='Valider', command = Verification)
        Bouton.pack(side = LEFT, padx = 5, pady = 5)
        Verification()
print('fin')

