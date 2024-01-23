import random
import sqlite3
class compte:
    numero=""
    for i  in range (15):
        numero=numero+str(random.randint(0,9))
        
    def __init__(self,nom,prenom,solde=0,numero=numero):
        self.numero=numero
        self.nom=nom
        self.prenom=prenom
        self.solde=solde
        
    def new_compte(self):
        con=sqlite3.connect("ma_Banque.db")
        cur=con.cursor()
        sql = "INSERT INTO compte (num, nom,prenom,solde) VALUES (?, ?,?, ?)"
        val = (self.numero,self.nom, self.prenom,self.solde)
        cur.execute(sql, val)
        con.commit()
        print("Compte crée avec succès!!")
    
    def retrait(mnt,num):
        con=sqlite3.connect("ma_Banque.db")
        cur=con.cursor()
        req=cur.execute("SELECT solde  FROM compte WHERE num=? ",(num,))
        result=req.fetchone()
        if(result[0]>mnt):
            retrait=cur.execute("UPDATE compte SET solde=? WHERE num=?",(result[0]-mnt,num))
            print("Retrait effectuer avec succes!!")
        else:
            print("Solde Insuffisant!!")
        con.commit() 

    def send(mnt,nume,numr):
        con=sqlite3.connect("ma_Banque.db")
        cur=con.cursor()
        req=cur.execute("SELECT solde  FROM compte WHERE num=? ",(nume,))
        result=req.fetchone()
        if(result[0]>mnt):
            reqe=cur.execute("UPDATE compte SET solde=? WHERE num=?",(result[0]-mnt,nume))
            reqre=cur.execute("SELECT solde  FROM compte WHERE num=? ",(numr,))
            result1=req.fetchone()
            reqr=cur.execute("UPDATE compte SET solde=? WHERE num=?",(result1[0]+mnt,numr))
            print("Envoyer avec succes!!")
        else:
            print("Solde Insuffisant!!")
        con.commit()
    
    def depot(mnt,num):
        con=sqlite3.connect("ma_Banque.db")
        cur=con.cursor()
        req=cur.execute("SELECT solde  FROM compte WHERE num=? ",(num,))
        result=req.fetchone()
        retrait=cur.execute("UPDATE compte SET solde=? WHERE num=?",(result[0]+mnt,num))
        con.commit() 
        print("depot effectuer avec succes!!")
               
    def getname(self,num):
        con=sqlite3.connect("ma_Banque.db")
        cur=con.cursor()
        req=cur.execute("SELECT nom,prenom FROM compte WHERE num=?",(num,))
        req.fetchall()
        for i in req:
            print("Nom: ",i[0],"\n Prenom: ",i[1])
            
    def solde(num):
        con=sqlite3.connect("ma_Banque.db")
        cur=con.cursor()
        req=cur.execute("SELECT solde  FROM compte WHERE num=? ",(num,))
        result=req.fetchone()
        for i in result:
            print(i)
        con.commit
    
    def aff_compte():
        con=sqlite3.connect("ma_Banque.db")
        cur=con.cursor()
        req="SELECT * FROM compte"
        request=cur.execute(req)
        resul=request.fetchall()
        for i in resul:
            print("num:",i[1],"\t","Nom:",i[2],"\t","Prenom:",i[3],"\t","Solde:",i[4],"CFA","\n")

    

def send(mnt,nume,numr):
    con=sqlite3.connect("ma_Banque.db")
    cur=con.cursor()
    req=cur.execute("SELECT solde  FROM compte WHERE num=? ",(nume,))
    result=req.fetchone()
    if(result[0]>mnt):
        reqe=cur.execute("UPDATE compte SET solde=? WHERE num=?",(result[0]-mnt,nume))
        reqre=cur.execute("SELECT solde  FROM compte WHERE num=? ",(numr,))
        result1=req.fetchone()
        reqr=cur.execute("UPDATE compte SET solde=? WHERE num=?",(result1[0]+mnt,numr))
        print("Envoyer avec succes!!")
    else:
        print("Solde Insuffisant!!")
    con.commit()
    
def retrait(mnt,num):
    con=sqlite3.connect("ma_Banque.db")
    cur=con.cursor()
    req=cur.execute("SELECT solde  FROM compte WHERE num=? ",(num,))
    result=req.fetchone()
    if(result[0]>mnt):
        retrait=cur.execute("UPDATE compte SET solde=? WHERE num=?",(result[0]-mnt,num))
        print("Retrait effectuer avec succes!!")
    else:
        print("Solde Insuffisant!!")
    con.commit()   
    
def depot(mnt,num):
    con=sqlite3.connect("ma_Banque.db")
    cur=con.cursor()
    req=cur.execute("SELECT solde  FROM compte WHERE num=? ",(num,))
    result=req.fetchone()
    retrait=cur.execute("UPDATE compte SET solde=? WHERE num=?",(result[0]+mnt,num))
    con.commit() 
    print("depot effectuer avec succes!!")


def aff_compte():
        con=sqlite3.connect("ma_Banque.db")
        cur=con.cursor()
        req="SELECT * FROM compte"
        request=cur.execute(req)
        resul=request.fetchall()
        for i in resul:
            print("num:",i[1],"\t","Nom:",i[2],"\t","Prenom:",i[3],"\t","Solde:",i[4],"CFA","\n")



#num="079077747036011"
#send(4000,str(num))
nume=897516190485004
numr=862028277635879
#depot(50000,nume)
#retrait(229000,numr)
#send(50000,nume,numr)




