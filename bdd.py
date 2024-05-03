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
        print("La base de données à était supprimer.")
    
    def delete_data(self, table, iden):
        try:
            self.curs.execute(requete.deletedata.format(table,f"id_{table}",iden))
            print("Donnée supprimée")
        except:
            print("La données n'a pas pu être supprimer.\nIl est possible que l'identificateur donné soit erroné.")
    
    def delete_double_id(self, table, table1, table2,id1, id2):
        try:
            self.curs.execute(requete.deletedoubleid.format(table,table1,id1,table2,id2))
            print("Donnée supprimée")
        except:
            print("La données n'a pas pu être supprimer.\nIl est possible que l'identificateur donné soit erroné.")

    
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
    
    def prin_data_with_where(self, sel,table, comp, test):
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
        self.curs.execute(requete.select_id_with_where.format(sel,table,comp,test))
        
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
        """
            csv fomrat nom_batiment;adresse;ville;code_postale;nom_salle
        """
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
    
    def creatcompositeur(self):
        """
            csv format nom_compositeur;date_naissance;date_mort;nb_morceau
        """
        with open(f"{self.chemin_csv}/compositeur.csv", 'r+') as file:
            read = csv.reader(file, delimiter=';')
            cpt=-1
            for elem in read:
                cpt+=1
                if cpt==0:
                    continue
                else:
                    datenai="NULL" if elem[1] =="NULL" else f"'{elem[1]}'"
                    datemor="NULL" if elem[2] =="NULL" else f"'{elem[2]}'"
                    nbmor="NULL" if elem[3] =="NULL" else f"'{elem[3]}'"
                    val=f"NULL,{elem[0]},{datenai},{datemor},{nbmor}"
                    self.curs.execute(requete.request_ajout.format("compositeur",requete.valeur["compositeur"],val))
            self.bd.commit()
    
    def creatmorceau(self):
        """
            csv format id_compositeur;nom_morceau;date_composition;durée_morceau;genre;lieu_compo
        """
        with open(f"{self.chemin_csv}/morceau.csv", 'r+') as file:
            read = csv.reader(file, delimiter=';')
            cpt=-1
            for elem in read:
                cpt+=1
                if cpt==0:
                    continue
                else:
                    self.curs.execute(requete.select_with_where.format("id_compositeur","compositeur","nom_compositeur",elem[0]))
                    id_comp=self.curs.fetchall()
                    datecomp="NULL" if elem[2] =="NULL" else f"'{elem[2]}'"
                    lieucomp="NULL" if elem[5] =="NULL" else f"'{elem[5]}'"
                    val=f"NULL,'{id_comp[0][0]}','{elem[1]}',{datecomp},'{elem[3]}','{elem[4]}',{lieucomp}"
                    self.curs.execute(requete.request_ajout.format("morceau",requete.valeur["morceau"],val))
            self.bd.commit()
    
    def creatconcert(self):
        """
            id_salle;nom_concert;date_concert;formation;nb_place_restante;chef_d_orchestre;soliste;prix_place;visuel;durée_concert;genre_concert
        """
        with open(f"{self.chemin_csv}/concert.csv", 'r+') as file:
            read = csv.reader(file, delimiter=';')
            cpt=-1
            for elem in read:
                cpt+=1
                if cpt==0:
                    continue
                else:
                    self.curs.execute(requete.select_with_where.format("id_salle","salle","nom_salle",elem[0]))
                    id_salle=self.curs.fetchall()
                    chef="NULL" if elem[5] =="NULL" else f"'{elem[5]}'"
                    soliste="NULL" if elem[6] =="NULL" else f"'{elem[6]}'"
                    prix="NULL" if elem[7] =="NULL" else f"'{elem[7]}'"
                    val=f"NULL,'{id_salle[0][0]}','{elem[1]}','{elem[2]}','{elem[3]}','{elem[4]}','{elem[5]}',{chef},{soliste},{prix},'{elem[8]}','{elem[9]}','{elem[10]}'"
                    self.curs.execute(requete.request_ajout.format("concert",requete.valeur["concert"],val))
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
