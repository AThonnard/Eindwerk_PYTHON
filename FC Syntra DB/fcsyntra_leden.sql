-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: fcsyntra
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `leden`
--

DROP TABLE IF EXISTS `leden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leden` (
  `lidNummer` int NOT NULL AUTO_INCREMENT,
  `voornaam` varchar(45) NOT NULL,
  `achternaam` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `land` varchar(45) NOT NULL,
  `postcode` int NOT NULL,
  `gemeente` varchar(45) NOT NULL,
  `straat` varchar(100) NOT NULL,
  `telefoon` varchar(45) NOT NULL,
  `gsm` varchar(45) NOT NULL,
  `aanspreking` varchar(45) NOT NULL,
  `taal` varchar(45) NOT NULL,
  `paswoord` blob NOT NULL,
  `pwd_key` blob NOT NULL,
  PRIMARY KEY (`lidNummer`),
  UNIQUE KEY `lidNummer_UNIQUE` (`lidNummer`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leden`
--

LOCK TABLES `leden` WRITE;
/*!40000 ALTER TABLE `leden` DISABLE KEYS */;
INSERT INTO `leden` VALUES (68,'Arnaud','Thonnard','a.t@gmlail.com','Algeria',3271,'Zichem','Vossenberg 30','02','Mobiel (optioneel)','Mevr.','Frans',_binary 'gAAAAABinxnX4zVP9zjURWHLky4ePdLVbB75AUur8bWRS0jjJLxzfVPXiwgJ1PTdmC7Ec6tTb6Njy1ZeKnCeK81mUY5JN-HbDw==',_binary 'tEqxLc04VJ371H-1CGQLmIFQIioQL0Q4jBdDeMOg5hI='),(69,'Bjorn','Lecis','b.j@gmail.com','Belgium',3600,'Genk','Vossestraat 41','089/112233','Mobiel (optioneel)','Dhr','Nederlands',_binary 'gAAAAABioOKroO5uBk5vO4lUp_jz6D9HNRX7kYeFj8MsrRnPsuxl9g5RzIwgQ2k0EB6HhbvE1KuN8thV9kHVnkybk5BkWAw3MA==',_binary 'kv3vUwOfRGcDMDyaW_s7TNbg25qEoBaoRpoZ6Cc6xJI=');
/*!40000 ALTER TABLE `leden` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-08 20:09:22
