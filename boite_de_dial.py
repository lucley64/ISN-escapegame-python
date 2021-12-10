# script mot_de_passe.py
from tkinter import *
from tkinter.messagebox import * # boîte de dialogue
def Verification():
    if Motdepasse.get() == 'a':
        # le mot de passe est bon : on affiche une boîte de dialogue puis on ferme la fenêtre
        showinfo('Résultat','Bravo le mot est correct.\nAu revoir !')
        Mafenetre.destroy()
    else:
        # le mot de passe est incorrect : on affiche une boîte de dialogue
        showwarning('Résultat','Désolé.\nVeuillez recommencer !')
        Motdepasse.set('')
# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Identification requise')
# Création d'un widget Label (texte 'Mot de passe')
Label1 = Label(Mafenetre, text = 'Mot à découvrir ')
Label1.pack(side = LEFT, padx = 5, pady = 5)
# Création d'un widget Entry (champ de saisie)
Motdepasse= StringVar()
Champ = Entry(Mafenetre, textvariable= Motdepasse, bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5)
# Création d'un widget Button (bouton Valider)
Bouton = Button(Mafenetre, text ='Valider', command = Verification)
Bouton.pack(side = LEFT, padx = 5, pady = 5)
Mafenetre.mainloop()