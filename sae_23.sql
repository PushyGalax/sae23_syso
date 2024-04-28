-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 07 avr. 2024 à 10:34
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `sae_23`
--

-- --------------------------------------------------------

--
-- Structure de la table `batiment`
--

CREATE TABLE `batiment` (
  `id_batiment` int(11) NOT NULL,
  `nom_batiment` varchar(200) NOT NULL,
  `adresse` varchar(200) NOT NULL,
  `ville` varchar(200) NOT NULL,
  `code_postale` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `compositeur`
--

CREATE TABLE `compositeur` (
  `id_compositeur` int(11) NOT NULL,
  `nom_compositeur` int(11) NOT NULL,
  `date_naissance` date NOT NULL,
  `date_mort` date DEFAULT NULL,
  `nb_morceau` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `concert`
--

CREATE TABLE `concert` (
  `id_concert` int(11) NOT NULL,
  `id_salle` int(11) NOT NULL,
  `nom_concert` varchar(150) NOT NULL,
  `date_concert` date NOT NULL,
  `formation` enum('orchestre symphonique','orchestre à vent','orchestre à corde','duo','trio','quatuor','soliste','rock','électro','spéciale') NOT NULL,
  `nb_place_restante` int(11) NOT NULL,
  `chef_d'orchestre` varchar(100) DEFAULT NULL,
  `soliste` varchar(100) DEFAULT NULL,
  `prix_place` float DEFAULT NULL,
  `visuel` tinyint(1) NOT NULL,
  `durée_concert` float NOT NULL COMMENT 'minute',
  `genre_concert` enum('symphonique','vent','corde','duo','trio','quatuor','soliste','rock','électro','spéciale') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `jouer`
--

CREATE TABLE `jouer` (
  `id_concert` int(11) NOT NULL,
  `id_morceau` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `morceau`
--

CREATE TABLE `morceau` (
  `id_morceau` int(11) NOT NULL,
  `id_compositeur` int(11) NOT NULL,
  `nom_morceau` text NOT NULL,
  `date_composition` text DEFAULT NULL COMMENT 'année',
  `durée_morceau` float NOT NULL COMMENT 'minutes',
  `genre` enum('concerto','composition','symphonie','sonate','quatuor','rock','électro','spéciale') NOT NULL,
  `lieu_compo` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

CREATE TABLE `reservation` (
  `id_reservation` int(11) NOT NULL,
  `id_concert` int(11) NOT NULL,
  `nom_reservation` varchar(50) NOT NULL,
  `prenom_reservation` varchar(50) NOT NULL,
  `place` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `salle`
--

CREATE TABLE `salle` (
  `id_salle` int(11) NOT NULL,
  `id_batiment` int(11) NOT NULL,
  `nom_salle` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `batiment`
--
ALTER TABLE `batiment`
  ADD PRIMARY KEY (`id_batiment`);

--
-- Index pour la table `compositeur`
--
ALTER TABLE `compositeur`
  ADD PRIMARY KEY (`id_compositeur`);

--
-- Index pour la table `concert`
--
ALTER TABLE `concert`
  ADD PRIMARY KEY (`id_concert`),
  ADD UNIQUE KEY `id_salle` (`id_salle`);

--
-- Index pour la table `jouer`
--
ALTER TABLE `jouer`
  ADD UNIQUE KEY `id_concert` (`id_concert`),
  ADD UNIQUE KEY `id_morceau` (`id_morceau`);

--
-- Index pour la table `morceau`
--
ALTER TABLE `morceau`
  ADD PRIMARY KEY (`id_morceau`),
  ADD UNIQUE KEY `id_compositeur` (`id_compositeur`);

--
-- Index pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`id_reservation`);

--
-- Index pour la table `salle`
--
ALTER TABLE `salle`
  ADD PRIMARY KEY (`id_salle`),
  ADD UNIQUE KEY `id_batiment` (`id_batiment`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `batiment`
--
ALTER TABLE `batiment`
  MODIFY `id_batiment` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `compositeur`
--
ALTER TABLE `compositeur`
  MODIFY `id_compositeur` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `concert`
--
ALTER TABLE `concert`
  MODIFY `id_concert` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `morceau`
--
ALTER TABLE `morceau`
  MODIFY `id_morceau` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `reservation`
--
ALTER TABLE `reservation`
  MODIFY `id_reservation` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `salle`
--
ALTER TABLE `salle`
  MODIFY `id_salle` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `batiment`
--
ALTER TABLE `batiment`
  ADD CONSTRAINT `batiment_ibfk_1` FOREIGN KEY (`id_batiment`) REFERENCES `salle` (`id_batiment`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `compositeur`
--
ALTER TABLE `compositeur`
  ADD CONSTRAINT `compositeur_ibfk_1` FOREIGN KEY (`id_compositeur`) REFERENCES `morceau` (`id_compositeur`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `concert`
--
ALTER TABLE `concert`
  ADD CONSTRAINT `concert_ibfk_1` FOREIGN KEY (`id_salle`) REFERENCES `salle` (`id_salle`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `jouer`
--
ALTER TABLE `jouer`
  ADD CONSTRAINT `jouer_ibfk_1` FOREIGN KEY (`id_concert`) REFERENCES `concert` (`id_concert`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `morceau`
--
ALTER TABLE `morceau`
  ADD CONSTRAINT `morceau_ibfk_1` FOREIGN KEY (`id_morceau`) REFERENCES `jouer` (`id_morceau`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`id_reservation`) REFERENCES `concert` (`id_concert`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
