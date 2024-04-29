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
        >>> a   :-> ajout de données"""


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
    date_conc = input("Date du concert\n >>> ")
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
    sql.prin_all_data_with_where("*","morceau", "compositeur", id_comp)
    id_morc=input(" >>> ")
    test=True
    while test:
        if int(id_morc) in sql.list_id_where("id_morceau","morceau","compositeur", id_comp):
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
    

if __name__ == "__main__":
    address, port, user, mdp, database = lireconf()
    port = int(port)

    print("connexion")
    sql = bdd.bdd(address, user, mdp, port,"./csv")
    print("connexion etablit\n")
    
    print("|-"+"-"*132+"-|")
    print(title)
    print("|-"+"-"*132+"-|\n")
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
            
            case _:
                print("La commande n'existe pas")

