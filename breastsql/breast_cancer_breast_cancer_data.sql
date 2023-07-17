-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: breast_cancer
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
-- Table structure for table `breast_cancer_data`
--

DROP TABLE IF EXISTS `breast_cancer_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `breast_cancer_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date_created` date NOT NULL,
  `radius` float DEFAULT NULL,
  `tm` float DEFAULT NULL,
  `pm` float DEFAULT NULL,
  `aream` int DEFAULT NULL,
  `smoothm` float DEFAULT NULL,
  `compm` float DEFAULT NULL,
  `con_m` float DEFAULT NULL,
  `cpm` float DEFAULT NULL,
  `sym` float DEFAULT NULL,
  `frac_m` float DEFAULT NULL,
  `radius_se` float DEFAULT NULL,
  `texture_se` int DEFAULT NULL,
  `pm_se` float DEFAULT NULL,
  `area_se` float DEFAULT NULL,
  `smooth_se` float DEFAULT NULL,
  `compact_se` float DEFAULT NULL,
  `con_se` float DEFAULT NULL,
  `cp_se` float DEFAULT NULL,
  `symmetry_se` float DEFAULT NULL,
  `fractal_se` float DEFAULT NULL,
  `radius_worst` float DEFAULT NULL,
  `texture_worst` float DEFAULT NULL,
  `pm_worst` float DEFAULT NULL,
  `area_worst` int DEFAULT NULL,
  `smooth_worst` float DEFAULT NULL,
  `compact_worst` float DEFAULT NULL,
  `con_worst` float DEFAULT NULL,
  `concavity_worst` float DEFAULT NULL,
  `symmetry_worst` float DEFAULT NULL,
  `fractal_worst` float DEFAULT NULL,
  `user` varchar(100) DEFAULT NULL,
  `result` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breast_cancer_data`
--

LOCK TABLES `breast_cancer_data` WRITE;
/*!40000 ALTER TABLE `breast_cancer_data` DISABLE KEYS */;
INSERT INTO `breast_cancer_data` VALUES (2,'2023-07-13',7,12,67,456,0.1,0.3,0.4,0.2,0.14,0.06,2,4,12,67,0.005,0.1,0.2,0.04,0.05,0.01,23,34,78,567,0.2,1,1,0.2,0.5,0.2,'priyanshubirthare99@gmail.com','Cancer Detected'),(3,'2023-07-13',7,12,67,456,0.1,0.3,0.4,0.2,0.14,0.06,2,4,12,67,0.005,0.1,0.2,0.04,0.05,0.01,23,34,78,567,0.2,1,1,0.2,0.5,0.2,'priyanshubirthare99@gmail.com','Cancer Detected'),(4,'2023-07-13',7,12,67,456,0.1,0.3,0.4,0.2,0.14,0.06,2,4,12,67,0.005,0.1,0.2,0.04,0.05,0.01,23,34,78,567,0.2,1,1,0.2,0.5,0.2,'priyanshubirthare99@gmail.com','Cancer Detected'),(5,'2023-07-13',7,12,67,456,0.1,0.3,0.4,0.2,0.14,0.06,2,4,12,67,0.005,0.1,0.2,0.04,0.05,0.01,23,34,78,567,0.2,1,1,0.2,0.5,0.2,'priyanshubirthare99@gmail.com','Cancer Detected'),(6,'2023-07-13',7,12,67,456,0.1,0.3,0.4,0.2,0.14,0.06,2,4,12,67,0.005,0.1,0.2,0.04,0.05,0.01,23,34,78,567,0.2,1,1,0.2,0.5,0.2,'priyanshubirthare99@gmail.com','Cancer Detected'),(7,'2023-07-13',7,12,67,456,0.1,0.3,0.4,0.2,0.14,0.06,2,4,12,67,0.005,0.1,0.2,0.04,0.05,0.01,23,34,78,567,0.2,1,1,0.2,0.5,0.2,'priyanshubirthare99@gmail.com','Cancer Detected'),(8,'2023-07-13',7,12,67,456,0.1,0.3,0.4,0.2,0.14,0.06,2,4,12,67,0.005,0.1,0.2,0.04,0.05,0.01,23,34,78,567,0.2,1,1,0.2,0.5,0.2,'priyanshubirthare99@gmail.com','cancer'),(9,'2023-07-13',7,12,67,456,0.1,0.3,0.4,0.2,0.14,0.06,2,4,12,67,0.005,0.1,0.2,0.04,0.05,0.01,23,34,78,567,0.2,1,1,0.2,0.5,0.2,'priyanshubirthare99@gmail.com','cancer');
/*!40000 ALTER TABLE `breast_cancer_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-14 12:43:42
