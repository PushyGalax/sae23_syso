import pymysql
import requete
import csv

class bdd:
    def __init__(self, address, login, mdp, port, chemin_csv='./csv') -> None:
        """
            Cette fonction va se connecter à la base de données
        """
        
        try:
            self.bd = pymysql.connect(host=address, port=port, user=login, password=mdp)
            self.curs = self.bd.cursor()
            self.chemin_csv = chemin_csv
            try:
                self.curs.execute("USE sae_23")
            except:
                print("Il faut créer la base")
        except:
            print("La connection n'a pas pu être établit.")
            exit(0)
            
    
    def drop(self):
        """
        Supprime la base de données en exécutant une requête DROP.

        Fonctionnement :
        - Exécute la requête de suppression (DROP) sur la base de données.
        - Communique avec la base de données pour effectuer les modifications.
        - Affiche un message indiquant que la base de données a été supprimée avec succès.
        """
        self.curs.execute(requete.drop)
        self.bd.commit()
        print("La base de données à était supprimer.")
    
    def delete_data(self, table, iden):
        """
        Supprime une entrée spécifique d'une table dans la base de données.

        Fonctionnement :
        - Exécute une requête de suppression (DELETE) pour supprimer une entrée spécifique dans une table.
        - Utilise les paramètres `table` et `iden` pour construire la requête de suppression.
        - Affiche un message de confirmation si la suppression est effectuée avec succès.
        - Gère les exceptions pour afficher un message approprié en cas d'échec de la suppression.
        """
        try:
            self.curs.execute(requete.deletedata.format(table,f"id_{table}",iden))
            print("Donnée supprimée")
        except:
            print("La données n'a pas pu être supprimer.\nIl est possible que l'identificateur donné soit erroné.")
    
    def delete_double_id(self, table, table1, table2,id1, id2):
        """
        Supprime une entrée spécifique en utilisant deux identifiants dans deux tables liées dans la base de données.

        Fonctionnement :
        - Exécute une requête de suppression (DELETE) pour supprimer une entrée spécifique dans une table `table`
        en utilisant deux identifiants (`id1` et `id2`) qui doivent correspondre respectivement aux tables `table1` et `table2`.
        - Cette fonctionnalité est utile pour supprimer des données dans des tables qui ont des relations via des clés étrangères.
        """
        try:
            self.curs.execute(requete.deletedoubleid.format(table,table1,id1,table2,id2))
            print("Donnée supprimée")
        except:
            print("La données n'a pas pu être supprimer.\nIl est possible que l'identificateur donné soit erroné.")

    
    def showall(self, table):
        """
        Affiche toutes les entrées d'une table spécifique dans la base de données.

        Fonctionnement :
        - Exécute une requête SELECT pour récupérer toutes les entrées de la table spécifiée (`table`).
        - Affiche les résultats formatés sous forme de tableau.
        """
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
        """
        Affiche des données spécifiques d'une table en fonction d'une condition de sélection.

        Fonctionnement :
        - Exécute une requête SELECT pour récupérer des données spécifiques (`sel`) de la table spécifiée (`table`)
        où la valeur de la colonne (`comp`) correspond à une condition (`test`).
        """
        self.curs.execute(requete.select_with_where.format(sel,table,comp,test))
        phrase=self.curs.fetchall()
        ph=""
        for elem in phrase:
            for val in elem:
                ph+=str(val)+" | "
            ph+="\n"
        print(ph)
            
    def return_all_id_from_table(self, table):
        """
        Récupère tous les identifiants (IDs) disponibles dans une table spécifique de la base de données.

        Fonctionnement :
        - Exécute une requête SELECT pour récupérer tous les identifiants (IDs) de la table spécifiée (`table`).
        """
        self.curs.execute(requete.list_all_id.format(table,table))
        
        idd=self.curs.fetchall()
        listeid=[]
        for elem in idd:
            listeid.append(elem[0])
        return listeid
    
    def list_id_where(self, sel, table, comp, test):
        """
        Récupère tous les identifiants (IDs) d'une table spécifique basés sur une condition de filtrage.

        Fonctionnement :
        - Exécute une requête SELECT pour récupérer tous les identifiants (IDs) de la colonne spécifiée (`sel`)
        de la table spécifiée (`table`) où la valeur de la colonne (`comp`) correspond à une condition (`test`).
        """
        self.curs.execute(requete.select_id_with_where.format(sel,table,comp,test))
        
        idd=self.curs.fetchall()
        listeid=[]
        for elem in idd:
            listeid.append(elem[0])
        return listeid
    
    def creat_database(self):
        """
        Crée la base de données et ses tables en utilisant les requêtes définies dans le fichier de requêtes.

        Fonctionnement :
        - Exécute les requêtes de création de base de données et de tables en utilisant les instructions SQL
        définies dans la liste `requete.creation` du fichier de requêtes.
        """
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

    def update(self, table, cle, valeur, id):
        """
        Met à jour une valeur spécifique dans une table donnée.

        Fonctionnement :
        - Exécute une requête UPDATE pour modifier la valeur d'une colonne spécifiée (`cle`)
        dans une table spécifique (`table`) pour une entrée spécifiée par son identifiant (`id`).
        """
        self.curs.execute(requete.update.format(table,cle,f"'{valeur}'" if valeur != "NULL" else "NULL", f"id_{table}",f"'{id}'"))
        self.bd.commit()
    
    def seljoinmor(self, sel, table1, table2, cle1, cle2, cond, test):
        """SELECT {} FROM {} JOIN {} ON {} = {} WHERE {} = {}"""
        self.curs.execute(requete.select_join.format(sel,table1,table2,cle1,cle2,cond,test))
        morce = self.curs.fetchall()
        self.curs.execute(requete.select_with_where.format("nom_concert","concert","id_concert",test))
        val=""
        for elem in morce:
            val+=elem[0]+", "
        print(f"Il y aura dans le concert {self.curs.fetchall()[0][0]} les morceaux {val[:-2]}.")
        
    def seljoincon(self, sel, table1, table2, cle1, cle2, cond, test):
        """SELECT {} FROM {} JOIN {} ON {} = {} WHERE {} = {}"""
        self.curs.execute(requete.select_join.format(sel,table1,table2,cle1,cle2,cond,test))
        conce = self.curs.fetchall()
        self.curs.execute(requete.select_with_where.format("nom_morceau","morceau","id_morceau",test))
        val=""
        for elem in conce:
            val+=elem[0]+", "
        print(f"Les concert où est présent le morceau {self.curs.fetchall()[0][0]} {'sont' if len(conce)>1 else "est" if len(conce)==1 else "est aucun"} {val[:-2]}.")
        
    def selform(self, form):
        self.curs.execute(requete.select_with_where.format("nom_concert","concert", "formation",f"'{form}'"))
        conce=self.curs.fetchall()
        val=""
        for elem in conce:
            val+=elem[0]+", "
        print(f"Les concert de formation instrumentale {form} {'sont' if len(conce)>1 else "est" if len(conce)==1 else "est aucun"} {val[:-2]}.")
        
    def selgenre(self, genre):
        self.curs.execute(requete.select_with_where.format("nom_concert","concert", "genre_concert",f"'{genre}'"))
        conce=self.curs.fetchall()
        val=""
        for elem in conce:
            val+=elem[0]+", "
        print(f"Les concert de formation genre {genre} {'sont' if len(conce)>1 else "est" if len(conce)==1 else "est aucun"} {val[:-2]}.")

    def selcomp(self, comp):
        """compositeur"""
        self.curs.execute(requete.select_triple_join.format("nom_concert","concert", "jouer", "concert.id_concert", "jouer.id_concert", "morceau", "jouer.id_morceau", "morceau.id_morceau", "compositeur", "morceau.id_compositeur", "compositeur.id_compositeur","compositeur.id_compositeur", comp))
        conce=self.curs.fetchall()
        val=""
        for elem in conce:
            val+=elem[0]+", "
        self.curs.execute(requete.select_with_where.format("nom_compositeur", "compositeur", "id_compositeur", comp))
        print(f"Les concert du compositeur {self.curs.fetchall()[0][0]} {'sont' if len(conce)>1 else "est" if len(conce)==1 else "est aucun"} {val[:-2]}.")
    
    def selville(self, ville):
        self.curs.execute(requete.select_double_join.format("nom_concert","concert","salle","concert.id_salle","salle.id_salle","batiment","salle.id_batiment","batiment.id_batiment","ville",f"'{ville}'"))
        conce=self.curs.fetchall()
        val=""
        for elem in conce:
            val+=elem[0]+", "
        print(f"Les concert de la ville {ville} {'sont' if len(conce)>1 else "est" if len(conce)==1 else "est aucun"} {val[:-2]}.")
        
    def add_valeur(self, table, *args):
        """
        Ajoute une nouvelle entrée (ligne) dans une table spécifiée avec les valeurs fournies.

        Fonctionnement :
        - Cette méthode génère et exécute une requête INSERT INTO pour ajouter une nouvelle entrée dans une table (`table`)
        avec les valeurs spécifiées (`args`).
        """
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
