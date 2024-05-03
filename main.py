import bdd as bdd

title = """|                                            /                       .-.                                                   /           |
|    .     .    .-. .  .-. .-.     .-.      /-.   .-._. .  .-.       `-'  .-.    .-.        .    .-._. .  .-.    .-.   ---/---  .-.    |
|   / \     )  /     )/   )   )    /  )    /   | (   )   )/   )     /    (      (  |       / \  (   )   )/   )  (  |     /     (  |    |
|  / ._)   (_.'     '/   /   (    /`-'  _.'    |  `-'   '/   (   _.(__.   `---'  `-'-'    / ._)  `-'   '/   (    `-'-'  /       `-'-'  |
| /      ..-._)               `-'/                            `-                         /                   `-                        |"""

def lireconf():
    with open("config.conf", 'r') as conf:
        file = conf.readlines()
        data=False
        listeinfo=[]
        for line in file:
            if line[0:3] == "###":
                continue
            elif line.strip() == "[bdd conf]":
                data=True
            elif data == True:
                listeinfo.append(line.strip().split(':')[1].strip())
        
    return listeinfo[0], listeinfo[1], listeinfo[2], listeinfo[3], listeinfo[4]

liste_table = ["batiment","salle","compositeur","concert","morceau","jouer"]

consigne = """  Voici les instructions de fonctionnement de l'application.
        >>> c   :-> donne les consignes de fonctionnement
        >>> q   :-> quitte l'application
        >>> d   :-> permet de drop la base de données, à exécuter dans le doute avant la création de la base de données
        >>> s   :-> permet de créer la base de données, les tables et de mettre les valeurs d'initiation
        >>> t   :-> permet de liste le contenue d'une table
        >>> r   :-> recherche
        >>> a   :-> ajout de données
        >>> x   :-> supprimer des données
        >>> u   :-> mettre à jours des données"""


def ajout_batiment():
    print("Ajout de batiment")
    nom_bat=input("Nom du batiment\n >>> ")
    addr_bat=input("Adresse du batiment\n >>> ")
    ville_bat=input("Ville du batiment\n >>> ")
    code_bat=input("Code postale du batiment\n >>> ")
    sql.add_valeur("batiment",nom_bat,addr_bat,ville_bat,code_bat)
    

def ajout_salle():
    print("Ajout d'une salle")
    print("Veuillez choisir l'id d'un batiment")
    sql.showall("batiment")
    id_bat=input(" >>> ")
    test=True
    while test:
        if int(id_bat) in sql.return_all_id_from_table("batiment"):
            test=False
        else:
            id_bat=input(" >>> ")
    nom_sal=input("Nom de la salle\n >>> ")
    sql.add_valeur("salle",id_bat,nom_sal)
            


def ajout_compositeur():
    print("Ajout de compositeur ou groupe")
    nom_comp=input("Nom du compositeur\n >>> ")
    dat_nais_comp=input("date de naissance du compositeur format AAAA/MM/JJ sinon NULL\n >>> ")
    if dat_nais_comp=="":
        dat_nais_comp="NULL"
    if dat_nais_comp=="NULL":
        dat_nais_comp+="µ"
    dat_mort_comp=input("date de mort du compositeur format AAAA/MM/JJ sinon NULL\n >>> ")
    if dat_mort_comp=="":
        dat_mort_comp="NULL"
    if dat_mort_comp=="NULL":
        dat_mort_comp+="µ"
    nb_comp=input("Nombre de composition sinon NULL\n >>> ")
    nb_comp+="µ"
    sql.add_valeur("compositeur",nom_comp,dat_nais_comp,dat_mort_comp,nb_comp)

def ajout_morceau():
    print("Ajout d'un morceau")
    print("Veuillez choisir l'id d'un compositeur")
    sql.showall("compositeur")
    id_com=input(" >>> ")
    test=True
    while test:
        if int(id_com) in sql.return_all_id_from_table("compositeur"):
            test=False
        else:
            id_com=input(" >>> ")
    nom_morc = input("Nom du morceau\n >>> ")
    annee_morc = input("Année de composition du morceau sinon NULL\n >>> ")
    if annee_morc=="":
        annee_morc="NULL"
    if annee_morc=="NULL":
        annee_morc+="µ"
    duree_morc = input("Durée du morceau en minutes\n >>> ")
    genre_morc = input("Genre du morceau parmi concerto, composition, symphonie, sonate, quatuor, rock, traditionnelle, électro, spéciale\n >>> ")
    test=True
    while test:
        if genre_morc not in ['concerto','composition','symphonie','sonate','quatuor','rock','électro','traditionnelle','spéciale']:
            genre_morc = input("Genre du morceau parmi concerto, composition, symphonie, sonate, quatuor, rock, traditionnelle, électro, spéciale\n >>> ")
        else:
            test=False
    lieu_morc = input("Lieu de composition du morceau en ville ou en pays sinon NULL\n >>> ")
    if lieu_morc=="":
        lieu_morc="NULL"
    if lieu_morc=="NULL":
        lieu_morc+="µ"
    sql.add_valeur("morceau",id_com,nom_morc,annee_morc,duree_morc,genre_morc,lieu_morc)

def ajout_concert():
    print("Ajout d'un concert")
    print("Veuillez choisir l'id d'une salle")
    sql.showall("salle")
    id_sal=input(" >>> ")
    test=True
    while test:
        if int(id_sal) in sql.return_all_id_from_table("salle"):
            test=False
        else:
            id_sal=input(" >>> ")
    nom_conc = input("Nom du concert\n >>> ")
    date_conc = input("Date du concert au format AAAA/MM/JJ\n >>> ")
    if date_conc=="":
        date_conc="NULL"
    if date_conc=="NULL":
        date_conc+="µ"
    form_conc = input("Formation instrumentale du concert parmi orchestre symphonique, orchestre à vent, orchestre à corde, duo, trio, quatuor, soliste, rock, traditionnelle, électro, spéciale\n >>> ")
    test=True
    while test:
        if form_conc not in ['orchestre symphonique','orchestre à vent','orchestre à corde','duo','trio','quatuor','soliste','rock','traditionnelle','électro','spéciale']:
            form_conc = input("Formation instrumentale du concert parmi orchestre symphonique, orchestre à vent, orchestre à corde, duo, trio, quatuor, soliste, rock, traditionnelle, électro, spéciale\n >>> ")
        else:
            test=False
    nbpl_conc = input("Nombre de place du concert\n >>> ")
    chef_conc = input("Chef d'orchestre du concert sinon NULL\n >>> ")
    if chef_conc=="":
        chef_conc="NULL"
    if chef_conc=="NULL":
        chef_conc+="µ"
    soli_conc = input("Soliste du concert sinon NULL\n >>> ")
    if soli_conc=="":
        soli_conc="NULL"
    if soli_conc=="NULL":
        soli_conc+="µ"
    prix_conc = input("Prix de la place en euro du concert sinon NULL\n >>> ")
    if prix_conc=="":
        prix_conc="NULL"
    if prix_conc=="NULL":
        prix_conc+="µ"
    visu_conc = input("Est ce que le concert contient de la dance ou des projections d'images? si oui 1 sinon 0\n >>> ")
    dure_conc = input("Durée du concert en minute\n >>> ")
    genr_conc = input("Genre du concert parmi symphonique, vent, corde, duo, trio, quatuor, soliste, rock, électro, traditionnelle, spéciale\n >>> ")
    test=True
    while test:
        if genr_conc not in ['symphonique','vent','corde','duo','trio','quatuor','soliste','rock','électro','traditionnelle','spéciale']:
            genr_conc = input("Genre du concert parmi symphonique, vent, corde, duo, trio, quatuor, soliste, rock, électro, traditionnelle, spéciale\n >>> ")
        else:
            test=False
    sql.add_valeur("concert",id_sal,nom_conc,date_conc,form_conc,nbpl_conc,chef_conc,soli_conc,prix_conc,visu_conc,dure_conc,genr_conc)

def ajout_jouer():
    print("Ajout d'un morceau à un concert")
    print("Veuillez choisir l'id d'un concert")
    sql.showall("concert")
    id_conc=input(" >>> ")
    test=True
    while test:
        if int(id_conc) in sql.return_all_id_from_table("concert"):
            test=False
        else:
            id_conc=input(" >>> ")
    print("Veuillez choisir l'id d'un compositeur")
    sql.showall("compositeur")
    id_comp=input(" >>> ")
    test=True
    while test:
        if int(id_comp) in sql.return_all_id_from_table("compositeur"):
            test=False
        else:
            id_comp=input(" >>> ")
    print("Veuillez choisir l'id d'un morceau")
    sql.prin_data_with_where("*","morceau", "id_compositeur", id_comp)
    id_morc=input(" >>> ")
    test=True
    while test:
        if int(id_morc) in sql.list_id_where("morceau","morceau","compositeur", id_comp):
            test=False
        else:
            id_morc=input(" >>> ")
    sql.add_valeur("jouer",id_conc,id_morc)
    


def ajout():
    print(f"veuiller choisir une table parmis les suivantes : {liste_table}")
    table_ajout=input(" >>> ").strip().lower()
    present=True
    while present:
        if table_ajout in liste_table:
            present=False
        else:
            print(f"veuiller choisir une table parmis les suivantes : {liste_table}")
            table_ajout=input(" >>> ").strip().lower()
    match table_ajout:
        case "batiment":
            ajout_batiment()
        
        case "salle":
            ajout_salle()
        
        case "compositeur":
            ajout_compositeur()
        
        case "concert":
            ajout_concert()
        
        case 'jouer':
            ajout_jouer()
        
        case 'morceau':
            ajout_morceau()
    

def delete():
    table=input(f"{liste_table}\nVeuillez choisir une table >>> ")
    testtable=True
    while testtable:
        if table not in liste_table:
            table=input(f"{liste_table}\nVeuillez choisir une table >>> ")
        else:
            testtable=False
    sql.showall(table)
    
    iden=input("Veuillez choisir l'identificateur de la donnée à supprimer, si c'est pour la table jouer, veuiller choisir les deux identifiants séparé pas une virgule comme suit: id_concert,id_morceau.\n >>> ")
    match table:
        case "batiment":
            id_salle=sql.list_id_where("salle","salle",table,iden)
            if len(id_salle)==0:
                sql.delete_data(table=table,iden=iden)
            else:
                peut_del=True
                print("Il y a encore des salles existantes pour le batiment, souhaitez vous les supprimer? (Y | N)")
                choice=input(" >>> ")
                if choice in ["Y","y"]:
                    for i in id_salle:
                        id_concert=sql.list_id_where("concert","concert","salle",i)
                        if len(id_concert)==0:
                            sql.delete_data("salle",i)
                        else:
                            print("La salle ne peut pas être supprimer car il y a un concert existant.\nVeuillez commencer pas supprimer d'abord les salles possédants des concerts.")
                            peut_del=False
                    if peut_del:
                        sql.delete_data(table=table,iden=iden)
                    else:
                        print("Le batiment n'est pas supprimer car il y a encore un concert attaché à une salle.")
        case "salle":
            id_concert=sql.list_id_where("concert","concert",table,iden)
            if len(id_concert)==0:
                sql.delete_data(table=table,iden=iden)
            else:
                peut_del=True
                print(f"Il y a encore des concerts existants pour la salle.\n{[sql.prin_data_with_where("*","concert","id_concert",i) for i in id_concert]}\nSouaitez vous les supprmier? (Y | N)")
                choice=input(" >>> ")
                if choice in ["Y","y"]:
                    for i in id_concert:
                        sql.delete_data("concert",i)
                    sql.delete_data(table=table,iden=iden)
                else:
                    print("La salle n'a pas était supprimer.")

        case "morceau":
            sql.delete_data(table=table,iden=iden)

        case "compositeur":
            ... ##################################################################################

        case "jouer":
            print("Le programme ne peut être modifié.")
        
        case "concert":
            sql.delete_data(table,iden)

        case _:
            print("La table n'existe pas.")

def updateable():
    print("Voici la liste des tables modifiables : concert, compositeur")
    choice=input("veuillez choisir une des tables modifiables.\n >>> ")
    match choice:
        case "concert":
            sql.showall("concert")
            id_=input("Veuillez choisir un id de concert existant.\n >>> ")
            while id_ not in sql.return_all_id_from_table("concert"):
                id_=input("Veuillez choisir un id de concert existant sinon l pour lister les concerts\n >>> ")
                if id_ == "l":
                    sql.showall("concert")
            print("Voici les clés modifiables pour la tables concert : date, place")
            cle=input("Veuillez choisir une clé.\n >>> ")
            match cle:
                case "date":
                    date=input("Veuillez choisir la nouvelles date du concert au format AAAA/MM/JJ sinon NULL\n >>> ")
                    sql.update(choice,"date_concert",date,id_)
                case "place":
                    ... ##################################################################################
                case _:
                    print("La clé demandée n'existe pas dans la table.")
        case "compositeur":
            ... ##################################################################################
        case _:
            print("Votre table n'est pas dans la liste des tables modifiables.")

                            

if __name__ == "__main__":
    address, port, user, mdp, database = lireconf()
    port = int(port)

    print("connexion")
    sql = bdd.bdd(address, user, mdp, port,"./csv")
    print("connexion etablit\n")
    
    print("--"+"-"*132+"--")
    print(title)
    print("--"+"-"*132+"--\n")
    print("                 Bienvenue dans le CLI de Symphonica Sonata\n\n")
    running=True
    print(consigne)
    while running:
        print()
        entree = input(" >>> ")
        match entree:
            case "q":
                running = False
                print("Merci d'avoir utilisé notre application")
                
            case "c":
                print(consigne)
                
            case "s":
                print("Création de la base de données et des tables")
                sql.creat_database()
                print("Création des salles et bâtiments")
                sql.creatsalle()
                
            case "d":
                print("Suppression de la base de données")
                sql.drop()
            
            case "t":
                print(liste_table)
                table=input("nom de la table >>> ")
                test=True
                while test:
                    if table.lower().strip() in liste_table:
                        test=False
                        sql.showall(table.lower().strip())
                    else:
                        table=input("nom d'une table existante >>> ")
            
            case "a":
                ajout()
            
            case "r":
                print("Work In Progress")
            
            case "x":
                delete()
            
            case "u":
                print("work in progress")
            
            case _:
                print("La commande n'existe pas")

