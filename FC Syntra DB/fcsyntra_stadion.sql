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
-- Table structure for table `stadion`
--

DROP TABLE IF EXISTS `stadion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stadion` (
  `plaatsID` varchar(5) NOT NULL,
  `tribune` varchar(2) NOT NULL,
  `rij` int NOT NULL,
  `stoel` int NOT NULL,
  `reserved` varchar(45) DEFAULT NULL,
  `reservationType` varchar(45) DEFAULT NULL,
  `prijsTicket` decimal(10,0) NOT NULL,
  PRIMARY KEY (`plaatsID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stadion`
--

LOCK TABLES `stadion` WRITE;
/*!40000 ALTER TABLE `stadion` DISABLE KEYS */;
INSERT INTO `stadion` VALUES ('A11','A',1,1,'Nee','',10),('A110','A',1,10,'Nee','',10),('A12','A',1,2,'Nee','',10),('A13','A',1,3,'Nee','',10),('A14','A',1,4,'Nee','',10),('A15','A',1,5,'Nee','',10),('A16','A',1,6,'Nee','',10),('A17','A',1,7,'Nee','',10),('A18','A',1,8,'Nee','',10),('A19','A',1,9,'Nee','',10),('A21','A',2,1,'Nee','',10),('A210','A',2,10,'Nee','',10),('A22','A',2,2,'Nee','',10),('A23','A',2,3,'Nee','',10),('A24','A',2,4,'Nee','',10),('A25','A',2,5,'Nee','',10),('A26','A',2,6,'Nee','',10),('A27','A',2,7,'Nee','',10),('A28','A',2,8,'Nee','',10),('A29','A',2,9,'Nee','',10),('B11','B',1,1,'Nee','',10),('B110','B',1,10,'Nee','',10),('B12','B',1,2,'Nee','',10),('B13','B',1,3,'Nee','',10),('B14','B',1,4,'Nee','',10),('B15','B',1,5,'Nee','',10),('B16','B',1,6,'Nee','',10),('B17','B',1,7,'Nee','',10),('B18','B',1,8,'Nee','',10),('B19','B',1,9,'Nee','',10),('B21','B',2,1,'Nee','',10),('B210','B',2,10,'Nee','',10),('B22','B',2,2,'Nee','',10),('B23','B',2,3,'Nee','',10),('B24','B',2,4,'Nee','',10),('B25','B',2,5,'Nee','',10),('B26','B',2,6,'Nee','',10),('B27','B',2,7,'Nee','',10),('B28','B',2,8,'Nee','',10),('B29','B',2,9,'Nee','',10),('C11','C',1,1,'Nee','',15),('C110','C',1,10,'Nee','',15),('C12','C',1,2,'Nee','',15),('C13','C',1,3,'Nee','',15),('C14','C',1,4,'Nee','',15),('C15','C',1,5,'Nee','',15),('C16','C',1,6,'Nee','',15),('C17','C',1,7,'Nee','',15),('C18','C',1,8,'Nee','',15),('C19','C',1,9,'Nee','',15),('C21','C',2,1,'Nee','',15),('C210','C',2,10,'Nee','',15),('C22','C',2,2,'Nee','',15),('C23','C',2,3,'Nee','',15),('C24','C',2,4,'Nee','',15),('C25','C',2,5,'Nee','',15),('C26','C',2,6,'Nee','',15),('C27','C',2,7,'Nee','',15),('C28','C',2,8,'Nee','',15),('C29','C',2,9,'Nee','',15),('D11','D',1,1,'Nee','',15),('D110','D',1,10,'Nee','',15),('D12','D',1,2,'Nee','',15),('D13','D',1,3,'Nee','',15),('D14','D',1,4,'Nee','',15),('D15','D',1,5,'Nee','',15),('D16','D',1,6,'Nee','',15),('D17','D',1,7,'Nee','',15),('D18','D',1,8,'Nee','',15),('D19','D',1,9,'Nee','',15),('D21','D',2,1,'Nee','',15),('D210','D',2,10,'Nee','',15),('D22','D',2,2,'Nee','',15),('D23','D',2,3,'Nee','',15),('D24','D',2,4,'Nee','',15),('D25','D',2,5,'Nee','',15),('D26','D',2,6,'Nee','',15),('D27','D',2,7,'Nee','',15),('D28','D',2,8,'Nee','',15),('D29','D',2,9,'Nee','',15),('E11','E',1,1,'Nee','',15),('E110','E',1,10,'Nee','',15),('E12','E',1,2,'Nee','',15),('E13','E',1,3,'Nee','',15),('E14','E',1,4,'Nee','',15),('E15','E',1,5,'Nee','',15),('E16','E',1,6,'Nee','',15),('E17','E',1,7,'Nee','',15),('E18','E',1,8,'Nee','',15),('E19','E',1,9,'Nee','',15),('E21','E',2,1,'Nee','',15),('E210','E',2,10,'Nee','',15),('E22','E',2,2,'Nee','',15),('E23','E',2,3,'Nee','',15),('E24','E',2,4,'Nee','',15),('E25','E',2,5,'Nee','',15),('E26','E',2,6,'Nee','',15),('E27','E',2,7,'Nee','',15),('E28','E',2,8,'Nee','',15),('E29','E',2,9,'Nee','',15),('F11','F',1,1,'Nee','',15),('F110','F',1,10,'Nee','',15),('F12','F',1,2,'Nee','',15),('F13','F',1,3,'Nee','',15),('F14','F',1,4,'Nee','',15),('F15','F',1,5,'Nee','',15),('F16','F',1,6,'Nee','',15),('F17','F',1,7,'Nee','',15),('F18','F',1,8,'Nee','',15),('F19','F',1,9,'Nee','',15),('F21','F',2,1,'Nee','',15),('F210','F',2,10,'Nee','',15),('F22','F',2,2,'Nee','',15),('F23','F',2,3,'Nee','',15),('F24','F',2,4,'Nee','',15),('F25','F',2,5,'Nee','',15),('F26','F',2,6,'Nee','',15),('F27','F',2,7,'Nee','',15),('F28','F',2,8,'Nee','',15),('F29','F',2,9,'Nee','',15),('G11','G',1,1,'Nee','',20),('G110','G',1,10,'Nee','',20),('G12','G',1,2,'Nee','',20),('G13','G',1,3,'Nee','',20),('G14','G',1,4,'Nee','',20),('G15','G',1,5,'Nee','',20),('G16','G',1,6,'Nee','',20),('G17','G',1,7,'Nee','',20),('G18','G',1,8,'Nee','',20),('G19','G',1,9,'Nee','',20),('G21','G',2,1,'Nee','',20),('G210','G',2,10,'Nee','',20),('G22','G',2,2,'Nee','',20),('G23','G',2,3,'Nee','',20),('G24','G',2,4,'Nee','',20),('G25','G',2,5,'Nee','',20),('G26','G',2,6,'Nee','',20),('G27','G',2,7,'Nee','',20),('G28','G',2,8,'Nee','',20),('G29','G',2,9,'Nee','',20),('H11','H',1,1,'Nee','',20),('H110','H',1,10,'Nee','',20),('H12','H',1,2,'Nee','',20),('H13','H',1,3,'Nee','',20),('H14','H',1,4,'Nee','',20),('H15','H',1,5,'Nee','',20),('H16','H',1,6,'Nee','',20),('H17','H',1,7,'Nee','',20),('H18','H',1,8,'Nee','',20),('H19','H',1,9,'Nee','',20),('H21','H',2,1,'Nee','',20),('H210','H',2,10,'Nee','',20),('H22','H',2,2,'Nee','',20),('H23','H',2,3,'Nee','',20),('H24','H',2,4,'Nee','',20),('H25','H',2,5,'Nee','',20),('H26','H',2,6,'Nee','',20),('H27','H',2,7,'Nee','',20),('H28','H',2,8,'Nee','',20),('H29','H',2,9,'Nee','',20);
/*!40000 ALTER TABLE `stadion` ENABLE KEYS */;
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
