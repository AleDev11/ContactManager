-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.27-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for contact_manager
CREATE DATABASE IF NOT EXISTS `contact_manager` /*!40100 DEFAULT CHARACTER SET utf32 COLLATE utf32_general_ci */;
USE `contact_manager`;

-- Dumping structure for table contact_manager.contacts
CREATE TABLE IF NOT EXISTS `contacts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_owner` int(11) NOT NULL DEFAULT 0,
  `name` varchar(255) NOT NULL DEFAULT '0',
  `lastname` varchar(255) NOT NULL DEFAULT '0',
  `number` int(11) NOT NULL DEFAULT 0,
  `birthday` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_contacts_user_accounts` (`id_owner`),
  CONSTRAINT `FK_contacts_user_accounts` FOREIGN KEY (`id_owner`) REFERENCES `user_accounts` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;

-- Dumping data for table contact_manager.contacts: ~13 rows (approximately)
INSERT INTO `contacts` (`id`, `id_owner`, `name`, `lastname`, `number`, `birthday`) VALUES
	(6, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(9, 5, 'Alberto', 'Perez', 846951759, '11/11/2000'),
	(10, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(11, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(12, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(13, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(14, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(15, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(16, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(17, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(18, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(19, 5, 'Alejandro', 'Font', 178936485, '11/01/2003'),
	(21, 8, 'Alejandro', 'Font', 0, '11/11/2003');

-- Dumping structure for table contact_manager.notes_contact
CREATE TABLE IF NOT EXISTS `notes_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `content` varchar(50) NOT NULL,
  `id_contact` int(11) NOT NULL DEFAULT 0,
  `id_owner` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `FK_notes_contact_contacts` (`id_contact`),
  KEY `FK_notes_contact_user_accounts` (`id_owner`),
  CONSTRAINT `FK_notes_contact_contacts` FOREIGN KEY (`id_contact`) REFERENCES `contacts` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_notes_contact_user_accounts` FOREIGN KEY (`id_owner`) REFERENCES `user_accounts` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;

-- Dumping data for table contact_manager.notes_contact: ~24 rows (approximately)
INSERT INTO `notes_contact` (`id`, `title`, `content`, `id_contact`, `id_owner`) VALUES
	(3, 'test', 'ssssssssssssssssssssss', 9, 5),
	(4, 'test', 'Esto es un test', 9, 5),
	(5, 'test', 'Esto es un test', 9, 5),
	(6, 'test', 'Esto es un test', 9, 5),
	(7, 'test', 'Esto es un test', 9, 5),
	(8, 'test', 'Esto es un test', 9, 5),
	(9, 'test', 'Esto es un test', 9, 5),
	(10, 'test', 'Esto es un test', 9, 5),
	(11, 'test', 'Esto es un test', 9, 5),
	(12, 'test', 'Esto es un test', 9, 5),
	(13, 'test', 'Esto es un test', 9, 5),
	(14, 'test', 'Esto es un test', 9, 5),
	(15, 'test', 'Esto es un test', 9, 5),
	(16, 'test', 'Esto es un test', 9, 5),
	(17, 'test', 'Esto es un test', 9, 5),
	(18, 'test', 'Esto es un test', 9, 5),
	(19, 'test', 'Esto es un test', 9, 5),
	(20, 'test', 'Esto es un test', 9, 5),
	(21, 'test', 'Esto es un test', 9, 5),
	(22, 'test', 'Esto es un test', 9, 5),
	(23, 'test', 'Esto es un test', 9, 5),
	(24, 'Hola', 'Hola', 6, 5),
	(25, 'Hola2', 'hola', 10, 5),
	(26, 'hola3', 'chao', 10, 5);

-- Dumping structure for table contact_manager.user_accounts
CREATE TABLE IF NOT EXISTS `user_accounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(55) NOT NULL,
  `name` varchar(55) NOT NULL DEFAULT '',
  `lastname` varchar(55) NOT NULL DEFAULT '',
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;

-- Dumping data for table contact_manager.user_accounts: ~4 rows (approximately)
INSERT INTO `user_accounts` (`id`, `email`, `name`, `lastname`, `password`) VALUES
	(5, 'admin@gmail.com', 'Admin', 'Administrador', '$2b$12$.SNNRQd0neb/k4DfuujBGuljLYAkxuqcbU3bOKyeDMcqvhFCOC9kG'),
	(6, 'will@gmail.com', 'Will', 'Peña', '$2b$12$.SNNRQd0neb/k4DfuujBGug2Zt1HxbEFXQ6UYlEOlz0zD7D4wZYQS'),
	(7, 'aledev@gmail.com', 'Alejandro', 'Font', '$2b$12$.SNNRQd0neb/k4DfuujBGug2Zt1HxbEFXQ6UYlEOlz0zD7D4wZYQS'),
	(8, 'ruben@gmail.com', 'Ruben', 'Bellido', '$2b$12$.SNNRQd0neb/k4DfuujBGug2Zt1HxbEFXQ6UYlEOlz0zD7D4wZYQS');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
