import bdd as bdd

title = """\
|                                            /                       .-.                                                   /           |
|    .     .    .-. .  .-. .-.     .-.      /-.   .-._. .  .-.       `-'  .-.    .-.        .    .-._. .  .-.    .-.   ---/---  .-.    |
|   / \     )  /     )/   )   )    /  )    /   | (   )   )/   )     /    (      (  |       / \  (   )   )/   )  (  |     /     (  |    |
|  / ._)   (_.'     '/   /   (    /`-'  _.'    |  `-'   '/   (   _.(__.   `---'  `-'-'    / ._)  `-'   '/   (    `-'-'  /       `-'-'  |
| /      ..-._)               `-'/                            `-                         /                   `-                        |"""

def lireconf():
    """
    Lit les informations de configuration à partir d'un fichier 'config.conf'.

    Fonctionnement :
    - Ouvre le fichier 'config.conf' en mode lecture.
    - Parcourt chaque ligne du fichier.
      - Ignore les lignes commençant par '###'.
      - Détecte le début de la section '[bdd conf]' pour commencer à récupérer les données.
      - Ajoute les informations de configuration à une liste `listeinfo` après le début de la section '[bdd conf]'.
    - Retourne les informations de configuration sous forme de tuple.
    """
    
    with open("./config.conf", 'r') as conf:
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
        
    return listeinfo[0], listeinfo[1], listeinfo[2], listeinfo[3], listeinfo[4], listeinfo[5]

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

conrecherche=""" Voici la liste des recherches disponibles actuellement au livrable CLI.
        >>> 1   :-> liste les morceaux d'un concert
        >>> 2   :-> liste les concerts d'un morceau
        >>> 3   :-> liste des concerts d'une formation
        >>> 4   :-> liste des concerts d'un genre musicale
        >>> 5   :-> liste des concerts de morceaux d'un compositeur ou d'un groupe
        >>> 6   :-> liste des concerts d'une ville
        >>> 7   :-> liste de tous les concerts par date
"""


def ajout_batiment():
    """
    Permet à l'utilisateur d'ajouter un nouveau bâtiment dans la table 'batiment' de la base de données.

    Fonctionnement :
    - Affiche un message indiquant qu'il s'agit de l'ajout d'un bâtiment.
    - Demande à l'utilisateur de saisir les détails du nouveau bâtiment :
      - Nom du bâtiment
      - Adresse du bâtiment
      - Ville du bâtiment
      - Code postal du bâtiment
    - Ajoute les détails du nouveau bâtiment dans la table "batiment" de la base de données en utilisant `sql.add_valeur()`.
    """
    print("Ajout de batiment")
    nom_bat=input("Nom du batiment\n >>> ")
    addr_bat=input("Adresse du batiment\n >>> ")
    ville_bat=input("Ville du batiment\n >>> ")
    code_bat=input("Code postale du batiment\n >>> ")
    sql.add_valeur("batiment",nom_bat,addr_bat,ville_bat,code_bat)
    

def ajout_salle():
    """
    Permet à l'utilisateur d'ajouter une nouvelle salle dans la table 'salle' de la base de données.

    Fonctionnement :
    - Affiche un message indiquant qu'il s'agit de l'ajout d'une salle.
    - Demande à l'utilisateur de choisir l'ID d'un bâtiment parmi ceux disponibles.
    - Affiche tous les bâtiments existants en utilisant `sql.showall("batiment")`.
    - Valide l'ID saisi en vérifiant s'il est présent dans la table des bâtiments.
    - Demande à l'utilisateur de saisir le nom de la nouvelle salle.
    - Ajoute les détails de la nouvelle salle dans la table "salle" de la base de données en utilisant `sql.add_valeur()`.
    """
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
    """
    Permet à l'utilisateur d'ajouter un nouveau compositeur ou groupe dans la table 'compositeur' de la base de données.

    Fonctionnement :
    - Affiche un message indiquant qu'il s'agit de l'ajout d'un compositeur ou groupe.
    - Demande à l'utilisateur de saisir les détails du nouveau compositeur ou groupe :
      - Nom du compositeur ou groupe
      - Date de naissance du compositeur au format AAAA/MM/JJ (peut être NULL)
      - Date de décès du compositeur au format AAAA/MM/JJ (peut être NULL)
      - Nombre de compositions du compositeur (peut être NULL)
    - Chaque détail saisi est validé selon les critères spécifiés.
    - Ajoute les détails du compositeur ou groupe dans la table "compositeur" de la base de données en utilisant `sql.add_valeur()`.
    """

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
    """
    Permet à l'utilisateur d'ajouter un nouveau morceau dans la table 'morceau' de la base de données.

    Fonctionnement :
    - Affiche un message indiquant qu'il s'agit de l'ajout d'un morceau.
    - Demande à l'utilisateur de choisir l'ID d'un compositeur parmi ceux disponibles.
    - Affiche tous les compositeurs existants en utilisant `sql.showall("compositeur")`.
    - Valide l'ID saisi en vérifiant s'il est présent dans la table des compositeurs.
    - Demande à l'utilisateur de saisir les détails du nouveau morceau :
      - Nom du morceau
      - Année de composition du morceau (peut être NULL)
      - Durée du morceau en minutes
      - Genre du morceau parmi les options spécifiées
      - Lieu de composition du morceau (ville ou pays, peut être NULL)
    - Chaque détail saisi est validé selon les critères spécifiés.
    - Ajoute les détails du morceau dans la table "morceau" de la base de données en utilisant `sql.add_valeur()`.
    """

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
    """
    Permet à l'utilisateur d'ajouter un nouveau concert dans la table 'concert' de la base de données.

    Fonctionnement :
    - Affiche un message indiquant qu'il s'agit de l'ajout d'un concert.
    - Demande à l'utilisateur de choisir l'ID d'une salle parmi celles disponibles.
    - Affiche tous les salles existantes en utilisant `sql.showall("salle")`.
    - Valide l'ID saisi en vérifiant s'il est présent dans la table des salles.
    - Demande à l'utilisateur de saisir les détails du nouveau concert :
      - Nom du concert
      - Date du concert au format AAAA/MM/JJ (peut être NULL)
      - Formation instrumentale du concert parmi les options spécifiées
      - Nombre de places disponibles pour le concert
      - Chef d'orchestre du concert (peut être NULL)
      - Soliste du concert (peut être NULL)
      - Prix de la place en euro du concert (peut être NULL)
      - Indication si le concert contient de la danse ou des projections d'images (1 pour oui, 0 pour non)
      - Durée du concert en minutes
      - Genre du concert parmi les options spécifiées
    - Chaque détail saisi est validé selon les critères spécifiés.
    - Ajoute les détails du concert dans la table "concert" de la base de données en utilisant `sql.add_valeur()`.
    """

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
    """
    Permet à l'utilisateur d'ajouter une association entre un morceau, un concert et un compositeur
    dans la table 'jouer' de la base de données.

    Fonctionnement :
    - Affiche un message indiquant qu'il s'agit de l'ajout d'un morceau à un concert.
    - Demande à l'utilisateur de choisir l'ID d'un concert parmi ceux disponibles.
    - Affiche tous les concerts existants en utilisant `sql.showall("concert")`.
    - Valide l'ID saisi en vérifiant s'il est présent dans la table des concerts.
    - Demande à l'utilisateur de choisir l'ID d'un compositeur parmi ceux disponibles.
    - Affiche tous les compositeurs existants en utilisant `sql.showall("compositeur")`.
    - Valide l'ID saisi en vérifiant s'il est présent dans la table des compositeurs.
    - Affiche les morceaux associés à ce compositeur en utilisant `sql.prin_data_with_where()` avec la table "morceau".
    - Demande à l'utilisateur de choisir l'ID d'un morceau parmi ceux associés à ce compositeur.
    - Valide l'ID saisi en vérifiant s'il est associé au compositeur choisi.
    - Ajoute l'association (concert, morceau) dans la table "jouer" en utilisant `sql.add_valeur()`.
    """
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
    """
    Permet à l'utilisateur d'ajouter des données dans une table spécifiée de la base de données.

    Fonctionnement :
    - Affiche à l'utilisateur la liste des tables disponibles où il peut ajouter des données.
    - Demande à l'utilisateur de choisir une table parmi celles disponibles.
    - Selon la table choisie, redirige l'utilisateur vers une fonction spécifique pour ajouter les données :
      - Si la table choisie est "batiment", appelle la fonction `ajout_batiment()`.
      - Si la table choisie est "salle", appelle la fonction `ajout_salle()`.
      - Si la table choisie est "compositeur", appelle la fonction `ajout_compositeur()`.
      - Si la table choisie est "concert", appelle la fonction `ajout_concert()`.
      - Si la table choisie est "jouer", appelle la fonction `ajout_jouer()`.
      - Si la table choisie est "morceau", appelle la fonction `ajout_morceau()`.
    """

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
    """
    Permet à l'utilisateur de supprimer des données d'une table spécifiée de la base de données.

    Fonctionnement :
    - Demande à l'utilisateur de choisir une table parmi celles disponibles dans la liste des tables.
    - Affiche les données de la table choisie à l'utilisateur.
    - Demande à l'utilisateur de saisir l'identifiant de la donnée qu'il souhaite supprimer.
    - Selon la table choisie, effectue des actions spécifiques de suppression :
      - Si la table est "batiment" :
        a. Vérifie s'il existe des salles associées au bâtiment à supprimer.
        b. Si aucune salle n'est associée, supprime le bâtiment directement.
        c. Si des salles existent, demande à l'utilisateur s'il souhaite également supprimer les salles et les concerts associés.
      - Si la table est "salle" :
        a. Vérifie s'il existe des concerts associés à la salle à supprimer.
        b. Si aucune concert n'est associé, supprime la salle directement.
        c. Si des concerts existent, demande à l'utilisateur s'il souhaite également supprimer les concerts associés.
      - Pour d'autres tables comme "morceau", "compositeur", et "concert", supprime la donnée directement.
      - Pour la table "compositeur", vérifie s'il existe des morceaux associés au compositeur à supprimer.
        - Si des morceaux existent, informe l'utilisateur que le compositeur ne peut pas être supprimé.
    """

    table=input(f"{liste_table}\nVeuillez choisir une table >>> ")
    testtable=True
    while testtable:
        if table not in liste_table:
            table=input(f"{liste_table}\nVeuillez choisir une table >>> ")
        else:
            testtable=False
    sql.showall(table)
    
    iden=input("Veuillez choisir l'identificateur de la donnée à supprimer\n >>> ")
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
            id_morceau=sql.list_id_where("morceau","morceau",table,iden)
            if len(id_morceau)==0:
                sql.delete_data(table=table,iden=iden)
            else:
                print("le compositeur ne peut être supprimer car il possède des musiques dans la table musique.")
                    
        case "jouer":
            print("Le programme ne peut être modifié.")
        
        case "concert":
            sql.delete_data(table,iden)

        case _:
            print("La table n'existe pas.")

def updateable():
    """
        Cette fonction permet à l'utilisateur de mettre à jour des données dans les tables 'concert' ou 'compositeur'
        de la base de données.

        Fonctionnement :
        1. Affiche les tables modifiables disponibles : 'concert', 'compositeur'.
        2. Demande à l'utilisateur de choisir une table à modifier.
        3. Selon le choix de l'utilisateur :
        - Si 'concert' est choisi :
            a. Affiche tous les concerts existants avec leurs IDs.
            b. Demande à l'utilisateur de saisir l'ID d'un concert existant.
            c. Propose les clés modifiables : 'date' (nouvelle date du concert) ou 'place' (nouveau nombre de places).
            d. Effectue la mise à jour dans la base de données en fonction de la clé choisie.
        - Si 'compositeur' est choisi :
            a. Affiche tous les compositeurs existants avec leurs IDs.
            b. Demande à l'utilisateur de saisir l'ID d'un compositeur existant.
            c. Demande à l'utilisateur de saisir la nouvelle date de décès du compositeur.
            d. Effectue la mise à jour dans la base de données pour la date de décès du compositeur.
    """

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
                    nbplace=input("Veuillez choisir le nouveau nombre de place disponible.\n >>> ")
                    while int(nbplace)<0:
                        nbplace=input("Le nombre doit être positif ou nul.\n >>> ")
                    sql.update("concert","date_concert",f"'{nbplace}'",id_)
                case _:
                    print("La clé demandée n'existe pas dans la table.")
        case "compositeur":
            sql.showall("compositeur")
            id_=input("Veuillez choisir un id d'un compositeur ou groupe existant.\n >>> ")
            while int(id_) not in sql.return_all_id_from_table("compositeur"):
                id_=input("Veuillez choisir un id d'un compositeur ou groupe existant sinon l pour lister les concerts\n >>> ")
                if id_ == "l":
                    sql.showall("compositeur")
            date=input("Veuillez choisir la date de mort du compositeur ou du groupe.\n >>> ")
            sql.update("compositeur","date_mort",date,id_)
        case _:
            print("Votre table n'est pas dans la liste des tables modifiables.")
            
def list_morceau_concert():
    """"SELECT {} FROM {} JOIN {} ON {} = {} WHERE {} = {}"""
    sql.showall("concert")
    id_=input("Veuillez choisir l'id d'un concert.\n >>> ")
    while id_ not in sql.return_all_id_from_table("concert"):
        id_=input("Veuillez choisir l'id d'un concert existant.\n >>> ")
    sql.seljoinmor('nom_morceau',"morceau","jouer","morceau.id_morceau","jouer.id_morceau","jouer.id_concert",id_)

def list_concert_morceau():
    """"SELECT {} FROM {} JOIN {} ON {} = {} WHERE {} = {}"""
    sql.showall("morceau")
    id_=input("Veuillez choisir l'id d'un morceau.\n >>> ")
    while int(id_) not in sql.return_all_id_from_table("morceau"):
        id_=input("Veuillez choisir l'id d'un morceau présent dans la table.\n >>> ")
    sql.seljoincon('nom_concert',"concert","jouer","concert.id_concert","jouer.id_concert","jouer.id_morceau",id_)

def list_concert_form():
    """formation"""
    forma=['orchestre symphonique','orchestre à vent','orchestre à corde','duo','trio','quatuor','soliste','rock','traditionnelle','électro','spéciale']
    print("Voici l'ensemble des formation possible : orchestre symphonique, orchestre à vent, orchestre à corde, duo, trio, quatuor, soliste, rock, traditionnelle, électro, spéciale")
    form=input("Veuillez en choisir un.\n >>> ")
    while form not in forma:
        form=input("Veuillez en choisir un présent dans la liste.\n >>> ")
    sql.selform(form)

def list_concert_genre():
    """genre"""
    genre=['symphonique','vent','corde','duo','trio','quatuor','soliste','rock','électro','traditionnelle','spéciale']
    print("Voici l'ensemble des genre possible : symphonique,vent,corde,duo,trio,quatuor,soliste,rock,électro,traditionnelle,spéciale")
    genr=input("Veuillez en choisir un.\n >>> ")
    while genr not in genre:
        genr=input("Veuillez en choisir un présent dans la liste.\n >>> ")
    sql.selgenre(genr)

def list_concert_comp():
    """compositeur"""
    sql.showall("compositeur")
    id_=input("Veuillez choisir l'id d'un compositeur.\n >>> ")
    while int(id_) not in sql.return_all_id_from_table("compositeur"):
        id_=input("Veuillez choisir l'id d'un compositeur existant.\n >>> ")
    sql.selcomp(id_)

def list_concert_lieu():
    """ville"""
    sql.selville(input("Veuillez séléctionner la ville du concert.\n >>> "))

def list_concert_date():
    import datetime
    print("Vous pouvez choisir une tranche de date ou bien tous les concerts supérieur à une date ou bien tous les concert inferieur à une date.")
    choice=input("Veuillez entrer 1 pour choisir dans une tranche, 2 pour choisir tous les concerts antérieur à une date, 3 pour tous les concerts supérieur à une date.")
    while choice not in ["1","2","3"]:
        choice=input("Veuillez entrer 1 pour choisir dans une tranche, 2 pour choisir tous les concerts antérieur à une date, 3 pour tous les concerts supérieur à une date.")
    match choice:
        case "1":
            date1=input("Veuillez choisir la date à partir de laquelle tous les concerts seront supérieur, au format AAAA-MM-JJ, sinon '' pour la date actuelle.\n >>> ")
            if date1=="":
                date1=datetime.datetime.now().strftime("%Y-%m-%d")
            date2=input("Veuillez choisir la date à partir de laquelle tous les concerts seront inferieur, au format AAAA-MM-DD.\n >>> ")
            while datetime.date(int(date1.split("-")[0]),int(date1.split("-")[1]),int(date1.split("-")[3])) > datetime.date(int(date2.split("-")[0]),int(date2.split("-")[1]),int(date2.split("-")[3])):
                print("La première date est plus grande que la deuxième.")
                date1=input("Veuillez choisir la date à partir de laquelle tous les concerts seront supérieur, au format AAAA-MM-JJ, sinon '' pour la date actuelle.\n >>> ")
                if date1=="":
                    date1=datetime.datetime.now().strftime("%Y-%m-%d")
                date2=input("Veuillez choisir la date à partir de laquelle tous les concerts seront inferieur, au format AAAA-MM-DD.\n >>> ")
            sql.seldatedeux(date1,date2)
        case "2":
            date1=input("Veuillez choisir la date à partir de laquelle tous les concerts seront antérieur, au format AAAA-MM-JJ, sinon '' pour la date actuelle.\n >>> ")
            if date1=="":
                date1=datetime.datetime.now().strftime("%Y-%m-%d")
            sql.seldateinf(date1)
        case "3":
            date1=input("Veuillez choisir la date à partir de laquelle tous les concerts seront supérieur, au format AAAA-MM-JJ, sinon '' pour la date actuelle.\n >>> ")
            if date1=="":
                date1=datetime.datetime.now().strftime("%Y-%m-%d")
            sql.seldatesup(date1)
    

def recherche():
    print(conrecherche)
    choice=input("Choisissez la recherche souhaitez.\n >>> ")
    match choice:
        case "1":
            list_morceau_concert()
        
        case "2":
            list_concert_morceau()
        
        case "3":
            list_concert_form()
        
        case "4":
            list_concert_genre()
        
        case "5":
            list_concert_comp()
        
        case "6":
            list_concert_lieu()
        
        case "7":
            list_concert_date()
        
        case _:
            print("Votre recherche n'est pas disponible.")

if __name__ == "__main__":
    address, port, user, mdp, database, chem = lireconf()
    port = int(port)

    print("connexion")
    sql = bdd.bdd(address, user, mdp, port,chem)
    print("connexion etablit\n")
    
    print("-"*136)
    print(title)
    print("-"*136+"\n")
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
                sql.creatcompositeur()
                sql.creatmorceau()
                sql.creatconcert()
                
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
                recherche()
            
            case "x":
                delete()
            
            case "u":
                updateable()
            
            case _:
                print("La commande n'existe pas")
                print(consigne)

