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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;

-- Dumping data for table contact_manager.contacts: ~2 rows (approximately)
INSERT INTO `contacts` (`id`, `id_owner`, `name`, `lastname`, `number`, `birthday`) VALUES
	(6, 6, 'Alejandro', 'Font', 654829865, '11/01/2003');

-- Dumping structure for table contact_manager.user_accounts
CREATE TABLE IF NOT EXISTS `user_accounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(55) NOT NULL,
  `name` varchar(55) NOT NULL DEFAULT '',
  `lastname` varchar(55) NOT NULL DEFAULT '',
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf32 COLLATE=utf32_general_ci;

-- Dumping data for table contact_manager.user_accounts: ~0 rows (approximately)
INSERT INTO `user_accounts` (`id`, `email`, `name`, `lastname`, `password`) VALUES
	(5, 'admin@gmail.com', 'Admin', 'Administrador', '$2b$12$.SNNRQd0neb/k4DfuujBGuljLYAkxuqcbU3bOKyeDMcqvhFCOC9kG'),
	(6, 'will@gmail.com', 'Will', 'Peña', '$2b$12$.SNNRQd0neb/k4DfuujBGug2Zt1HxbEFXQ6UYlEOlz0zD7D4wZYQS'),
	(7, 'aledev@gmail.com', 'Alejandro', 'Font', '$2b$12$.SNNRQd0neb/k4DfuujBGug2Zt1HxbEFXQ6UYlEOlz0zD7D4wZYQS');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
