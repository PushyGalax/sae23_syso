import bdd as bdd

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

address, port, user, mdp, database, chem = lireconf()
port = int(port)

print("connexion")
sql = bdd.bdd(address, user, mdp, port,chem)
print("connexion etablit\n")

sql.curs.execute("SELECT * FROM jouer")
all=sql.curs.fetchall()
with open("./csv/jouer.csv", 'w') as file:
    file.write("id_concert; id_morceau\n")
    for elem in all:
        sql.curs.execute(f"SELECT nom_concert FROM concert WHERE id_concert  = {elem[0]}")
        nomcon=sql.curs.fetchall()[0][0]
        sql.curs.execute(f"SELECT nom_morceau FROM morceau WHERE id_morceau  = {elem[1]}")
        nommor=sql.curs.fetchall()[0][0]
        file.write(f"{nomcon};{nommor}\n")

