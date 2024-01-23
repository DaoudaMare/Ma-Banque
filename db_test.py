import sqlite3

con=sqlite3.connect("ma_Banque.db")
cur=con.cursor()
sql = "INSERT INTO compte (num, nom,prenom,solde) VALUES (?, ?,?, ?)"
val = (12,"Mare", "Daouda",12000)
cur.execute(sql, val)

con.commit()
""""
def retrait(self,mnt,num):
        if(self.solde>mnt):
            with open ("compte", "r") as file:
                contenu=file.readlines()
                for i in contenu:
                    i=i.split("/")
                    if(str(num)==i[0]):
                        int(i[3])-mnt
                    else:
                        print("Numero de compte invalide!!")
                        


def aff_compte():
    with open("compte.txt","r") as file:
        info=file.readlines()
        for i in info:
            i=i.split("/")
            print("numero du compte:",i[0],"\t","Nom:",i[1],"\t","Prenom: ",i[2],"\t","Solde: ",i[3],"\n")
            

def send(mnt,num):
        with open("compte.txt","r") as file:
            containt=file.readlines()
            #print(containt[1].split("/"))
            for i in range(len(containt)-1):
                el=containt[i].split("/")
                if(str(num)==el[0]): 
                    copi=el
                    del el
                    copi[3]=int(copi[3])+mnt
                    with open("compte.txt","w+") as file:
                        for i in range(len(copi)-1):
                            elem=copi[0]+"/"+copi[1]+"/"+copi[2]+"/"+str(copi[3])
                        file.write(str(elem))
                        file.close()
                    print("Envoyer avec succés!! au ",num)
                    break
                else:
                    print("Numero de compte Invalide!!")
                    break
            file.close()
        

"""