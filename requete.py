creation = ["CREATE DATABASE IF NOT EXISTS sae_23",

            "CREATE TABLE IF NOT EXISTS batiment ("\
            "id_batiment int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,"\
            "nom_batiment varchar(300) NOT NULL,"\
            "adresse varchar(300) NOT NULL,"\
            "ville varchar(200) NOT NULL,"\
            "code_postale varchar(5) NOT NULL);",
            
            "CREATE TABLE IF NOT EXISTS salle ("\
            "id_salle int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,"\
            "id_batiment int(11) NOT NULL,"\
            "nom_salle varchar(300) NOT NULL,"\
            "INDEX (id_batiment),"\
            "CONSTRAINT FK_id_batiment FOREIGN KEY (id_batiment) REFERENCES batiment(id_batiment) ON DELETE CASCADE ON UPDATE CASCADE);",
            
            "CREATE TABLE IF NOT EXISTS concert ("\
            "id_concert int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,"\
            "id_salle int(11) NOT NULL,"\
            "nom_concert varchar(250) NOT NULL,"\
            "date_concert date NOT NULL,"\
            "formation enum('orchestre symphonique','orchestre à vent','orchestre à corde','duo','trio','quatuor','soliste','rock','traditionnelle','électro','spéciale') NOT NULL,"\
            "nb_place_restante int(11) NOT NULL,"\
            "chef_d_orchestre varchar(300) DEFAULT NULL,"\
            "soliste varchar(300) DEFAULT NULL,"\
            "prix_place float DEFAULT NULL,"\
            "visuel tinyint(1) NOT NULL,"\
            "durée_concert float NOT NULL COMMENT 'minute',"\
            "genre_concert enum('symphonique','vent','corde','duo','trio','quatuor','soliste','rock','électro','traditionnelle','spéciale') NOT NULL,"\
            "INDEX (id_salle),"\
            "CONSTRAINT FK_id_salle FOREIGN KEY (id_salle) REFERENCES salle(id_salle) ON UPDATE CASCADE);",
            
            "CREATE TABLE IF NOT EXISTS compositeur ("\
            "id_compositeur int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,"\
            "nom_compositeur varchar(300) NOT NULL,"\
            "date_naissance date DEFAULT NULL,"\
            "date_mort date DEFAULT NULL,"\
            "nb_morceau int(11) DEFAULT NULL);",
            
            "CREATE TABLE IF NOT EXISTS morceau ("\
            "id_morceau int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,"\
            "id_compositeur int(11) NOT NULL,"\
            "nom_morceau varchar(400) NOT NULL,"\
            "date_composition varchar(4) DEFAULT NULL COMMENT 'année',"\
            "durée_morceau float NOT NULL COMMENT 'minutes',"\
            "genre enum('concerto','composition','symphonie','sonate','quatuor','rock','électro','traditionnelle','spéciale') NOT NULL,"\
            "lieu_compo varchar(200) DEFAULT NULL,"\
            "INDEX (id_compositeur),"\
            "CONSTRAINT FK_id_compositeur FOREIGN KEY (id_compositeur) REFERENCES compositeur(id_compositeur) ON DELETE CASCADE ON UPDATE CASCADE);",
            
            "CREATE TABLE IF NOT EXISTS jouer ("\
            "id_concert int(11) NOT NULL,"\
            "id_morceau int(11) NOT NULL,"\
            "INDEX (id_concert),"\
            "INDEX (id_morceau),"\
            "CONSTRAINT FK_id_concert FOREIGN KEY (id_concert) REFERENCES concert(id_concert) ON DELETE CASCADE ON UPDATE CASCADE,"\
            "CONSTRAINT FK_id_morceau FOREIGN KEY (id_morceau) REFERENCES morceau(id_morceau) ON DELETE CASCADE ON UPDATE CASCADE);",
                        
            "CREATE TABLE IF NOT EXISTS reservation ("\
            "id_reservation int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,"\
            "id_concert int(11) NOT NULL,"\
            "nom_reservation varchar(150) NOT NULL,"\
            "prenom_reservation varchar(150) NOT NULL,"\
            "place int(11) DEFAULT NULL,"\
            "UNIQUE (id_concert),"\
            "CONSTRAINT FK_id_concert_deux FOREIGN KEY (id_concert) REFERENCES concert(id_concert) ON DELETE CASCADE ON UPDATE CASCADE);",
]

drop="DROP DATABASE sae_23"
request_ajout="INSERT INTO {}({}) VALUES({})"
deletedata="DELETE FROM {} WHERE {} = {}"
deletedoubleid="DELETE FROM {} WHERE id_{} = {} AND id_{} = {}"
select_id_with_where="SELECT id_{} FROM {} WHERE id_{} = {}"
select_with_where="SELECT DISTINCT {} FROM {} WHERE {} = {}"
select_key="SELECT DISTINCT {} FROM {}"
comp_inf="WHERE {} < {}"
comp_sup="WHERE {} > {}"
order="ORDER BY {}"
select_join="SELECT DISTINCT {} FROM {} JOIN {} ON {} = {} WHERE {} = {}"
select_double_join="SELECT DISTINCT {} FROM {} JOIN {} ON {} = {} JOIN {} ON {} = {} WHERE {} = {}"
select_triple_join="SELECT DISTINCT {} FROM {} JOIN {} ON {} = {} JOIN {} ON {} = {} JOIN {} ON {} = {} WHERE {} = {}"
update="UPDATE {} SET {}={} WHERE {}={}"

valeur={
"salle":"id_salle, id_batiment, nom_salle",
"batiment":"id_batiment, nom_batiment, adresse, ville, code_postale",
"compositeur":"id_compositeur, nom_compositeur, date_naissance, date_mort, nb_morceau",
"concert":"id_concert, id_salle, nom_concert, date_concert, formation, nb_place_restante, chef_d_orchestre, soliste, prix_place, visuel, durée_concert, genre_concert",
"jouer":"id_concert, id_morceau",
"morceau":"id_morceau, id_compositeur, nom_morceau, date_composition, durée_morceau, genre, lieu_compo"
}