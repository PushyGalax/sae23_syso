import pymysql
import requete
import csv

class bdd:
    def __init__(self, address, login, mdp, port, chemin_csv='./csv') -> None:
        """
            Cette fonction va se connecter à la base de données
        """
        self.bd = pymysql.connect(host=address, port=port, user=login, password=mdp)
        self.curs = self.bd.cursor()
        self.chemin_csv = chemin_csv
        try:
            self.curs.execute("USE sae_23")
        except:
            print("Il faut créer la base")
            
    
    def drop(self):
        self.curs.execute(requete.drop)
        self.bd.commit()
    
    def showall(self, table):
        self.curs.execute(requete.list_all_table.format(table))
        phrase=self.curs.fetchall()
        print(requete.valeur[table].replace(","," |"))
        ph=""
        for elem in phrase:
            for val in elem:
                ph+=str(val)+" | "
            ph+="\n"
        print(ph)
    
    def prin_all_data_with_where(self, sel,table, comp, test):
        self.curs.execute(requete.select_with_where.format(sel,table,comp,test))
        phrase=self.curs.fetchall()
        ph=""
        for elem in phrase:
            for val in elem:
                ph+=str(val)+" | "
            ph+="\n"
        print(ph)
        
    
    def return_all_id_from_table(self, table):
        self.curs.execute(requete.list_all_id.format(table,table))
        
        idd=self.curs.fetchall()
        listeid=[]
        for elem in idd:
            listeid.append(elem[0])
        return listeid
    
    def list_id_where(self, sel, table, comp, test):
        self.curs.execute(requete.select_with_where.format(sel,table,comp,test))
        
        idd=self.curs.fetchall()
        listeid=[]
        for elem in idd:
            listeid.append(elem[0])
        return listeid
    
    def creat_database(self):
        taille=len(requete.creation)
        try:
            self.curs.execute(requete.creation[0])
        except pymysql.err.ProgrammingError:
            pass
        self.curs.execute("USE sae_23")
        
        for i in range(1,taille):
            try:
                self.curs.execute(requete.creation[i])
            except pymysql.err.ProgrammingError:
                continue
        self.bd.commit()
    
    def creatsalle(self):
        with open(f"{self.chemin_csv}/batimentsalle.csv", 'r+') as file:
            read = csv.reader(file, delimiter=';')
            cpt=-1
            for elem in read:
                cpt+=1
                if cpt==0:
                    continue
                else:
                    val="NULL,'"+str(elem[0])+"','"+str(elem[1])+"','"+str(elem[2])+"','"+str(elem[3])+"'"
                    self.curs.execute(requete.request_ajout.format("batiment",requete.valeur["batiment"],val))
                    
                    self.curs.execute(f"SELECT id_batiment FROM batiment WHERE adresse = '{elem[1]}'")
                    id = self.curs.fetchall()
                    # print(id[0][0])
                    if len(elem) == 5:
                        salle=elem[4].split(',')
                        for sal in salle:
                            val="NULL,'"+str(id[0][0])+"','"+str(sal)+"'"
                            self.curs.execute(requete.request_ajout.format("salle",requete.valeur["salle"],val))
            self.bd.commit()
    
    def add_valeur(self, table, *args):
        if table not in ["jouer","reservation"]:
            val="NULL,"
            for elem in range(len(args)):
                if args[elem][-1]=="µ":
                    val+=f"{args[elem][:-1]},"
                else:
                    val+=f"'{args[elem]}',"
        else:
            val=""
            for elem in range(len(args)):
                if args[elem][-1]=="µ":
                    val+=f"{args[elem][:-1]},"
                else:
                    val+=f"'{args[elem]}',"

        
        print(requete.request_ajout.format(table,requete.valeur[table],val[:-1]))
        self.curs.execute(requete.request_ajout.format(table,requete.valeur[table],val[:-1]))
        self.bd.commit()
