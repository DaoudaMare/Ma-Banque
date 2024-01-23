from tkinter import *
from tkinter import messagebox
import customtkinter
from py import *

root=Tk()
#CONFIGURATION DE LA FENETRE

customtkinter.set_appearance_mode("Dark")
root.title("Ma Banque")
root.geometry("1300x800")
root.config(bg="#B3FFE0")

#FONCTIONS
def create():
    enreg=compte(nomE.get(),prenomE.get(),int(sold.get()))
    enreg.new_compte()
    msg=customtkinter.CTkLabel(box3,text="Compte crée avec succès!!",text_color="green",font=("Arial",20))
    msg.pack(pady=15)
     
def sends():
    compte.send(int(mntE.get()),numE.get(),numEr.get())
    msg=customtkinter.CTkLabel(box4,text="Envoyer avec succès!!",text_color="green",font=("Arial",15))
    msg.pack()
    
def operation():
    if(select1_var.get()=="on" and select2_var.get()=="off"):
        compte.retrait(int(lab2E.get()),lab1E.get())
        msg=customtkinter.CTkLabel(box5,text="Retrait effectuer avec succès!!",text_color="green",font=("Arial",15))
        msg.pack()
    elif(select2_var.get()=="on" and select1_var.get()=="off"):
        compte.depot(int(lab2E.get()),lab1E.get())
        msg=customtkinter.CTkLabel(box5,text="Depot effectuer avec succès!!",text_color="green",font=("Arial",15))
        msg.pack()
    else:
        msg=customtkinter.CTkLabel(box5,text="Choix invalid!!",text_color="green",font=("Arial",15))
        msg.pack()
  

def exit():
    label=messagebox.askyesno("exit","Voulez vous quittez?")
    if(label):
        root.quit()

def aff():
        con=sqlite3.connect("ma_Banque.db")
        cur=con.cursor()
        req="SELECT * FROM compte"
        request=cur.execute(req)
        resul=request.fetchall()
        for i in resul:
            list.insert(END,i)

#LES BOITES
box1=Frame(root,height=80,width=1300,bg="#00FF96")
box1.pack()
box1.propagate(False)

box2=LabelFrame(root,text="Nouveau Compte",height=350,width=600)
box2.place(x=0,y=90)
box2.propagate(False)



title=customtkinter.CTkLabel(box1,text="Gestion de Comptes Bancaires",font=("Arial",50),text_color="black")
title.pack(expand=YES)

open=customtkinter.CTkLabel(box2,text="Ouverture de compte",text_color="red",font=("Arial",30))
open.pack()

box3=Frame(box2)
box3.pack(pady=15)

box4=LabelFrame(root,text="Transfert",height=320,width=550)
box4.place(x=650,y=90)
box4.propagate(False)

box5=LabelFrame(root,text="Depot-Retrait",height=320,width=550)
box5.place(x=650,y=420)
box5.propagate(False)

box6=Scrollbar(root)
box6.pack()

list=Listbox(root,yscrollcommand=box6.set,width=100,height=100,font=("Arial",20))
list.place(x=0,y=450)
list.propagate(False)

nom=customtkinter.CTkLabel(box3,text="Nom: ",font=("Arial",20),text_color="black")
nom.pack()
nomE=customtkinter.CTkEntry(box3,placeholder_text="nom")
nomE.pack()

prenom=customtkinter.CTkLabel(box3,text="Prenom: ",font=("Arial",20),text_color="black")
prenom.pack()
prenomE=customtkinter.CTkEntry(box3,placeholder_text="prenom")
prenomE.pack()

soldel=customtkinter.CTkLabel(box3,text="Solde: ",font=("Arial",20),text_color="black")
soldel.pack()

sold=customtkinter.CTkEntry(box3,placeholder_text="0 CFA",placeholder_text_color="white")
sold.pack()

cree=customtkinter.CTkButton(box3,text="Créer",command=create)
cree.pack(pady=10)

affich=customtkinter.CTkButton(box3,text="Liste compte",command=aff)
affich.pack(pady=10)

#BOX POUR ENVOYER DE L'ARGENT

env=customtkinter.CTkLabel(box4,text="Transfert",text_color="red",font=("Arial",30))
env.pack()

num=customtkinter.CTkLabel(box4,text="Numero",text_color="black",font=("Arial",15))
num.pack(pady=5)
numE=customtkinter.CTkEntry(box4,placeholder_text="numero compte")
numE.pack()

numr=customtkinter.CTkLabel(box4,text="Numero du destinataire",text_color="black",font=("Arial",15))
numr.pack(pady=5)
numEr=customtkinter.CTkEntry(box4,placeholder_text="numero compte")
numEr.pack()

mnt=customtkinter.CTkLabel(box4,text="Montant de depot",text_color="black",font=("Arial",15))
mnt.pack(pady=5)
mntE=customtkinter.CTkEntry(box4,placeholder_text="0-CFA")
mntE.pack()

valid=customtkinter.CTkButton(box4,text="Envoyer",command=sends)
valid.pack(pady=5)

#BOX5 POUR RETRAIT ET DEPOT
opL=customtkinter.CTkLabel(box5,text="Dépot et Retrait",text_color="red",font=("Arial",30))
opL.pack()

lab1=customtkinter.CTkLabel(box5,text="Numero de compte",text_color="black",font=("Arial",15))
lab1.pack(pady=5)
lab1E=customtkinter.CTkEntry(box5,placeholder_text="Numero de compte")
lab1E.pack()

lab2=customtkinter.CTkLabel(box5,text="Montant",text_color="black",font=("Arial",15))
lab2.pack(pady=5)
lab2E=customtkinter.CTkEntry(box5,placeholder_text="Montant")
lab2E.pack()

select1_var=customtkinter.StringVar(value="on")
select1=customtkinter.CTkCheckBox(box5,text="Retrait",text_color="black",font=("Arial",15),variable=select1_var,onvalue="on",offvalue="off")
select1.pack(pady=5)

select2_var=customtkinter.StringVar(value="off")
select2=customtkinter.CTkCheckBox(box5,text="Dépot",text_color="black",font=("Arial",15),variable=select2_var,onvalue="on",offvalue="off")
select2.pack()

submit=customtkinter.CTkButton(box5,text="Effectuer",command=operation)
submit.pack(pady=5)

quitter=customtkinter.CTkButton(root,text="Quitter",hover_color="red",text_color="Black",font=("Arial",25),command=exit)
quitter.place(x=1150,y=750)
root.mainloop()