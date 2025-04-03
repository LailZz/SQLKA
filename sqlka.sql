CREATE DATABASE  IF NOT EXISTS `users` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `users`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: users
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `districts`
--

DROP TABLE IF EXISTS `districts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `districts` (
  `district_code` int NOT NULL,
  `district_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`district_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `districts`
--

LOCK TABLES `districts` WRITE;
/*!40000 ALTER TABLE `districts` DISABLE KEYS */;
INSERT INTO `districts` VALUES (101,'Деснянський'),(102,'Шевченківський'),(103,'Голосіївський'),(104,'Оболонський'),(105,'Печерський'),(106,'Подільський'),(107,'Святошинський');
/*!40000 ALTER TABLE `districts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `pensioner_id` int DEFAULT NULL,
  `pension_code` int DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `additional_payment` decimal(10,2) DEFAULT NULL,
  `additional_info` text,
  PRIMARY KEY (`payment_id`),
  KEY `pensioner_id` (`pensioner_id`),
  KEY `pension_code` (`pension_code`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`pensioner_id`) REFERENCES `pensioners` (`pensioner_id`),
  CONSTRAINT `payments_ibfk_2` FOREIGN KEY (`pension_code`) REFERENCES `pensions` (`pension_code`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,1,201,5000.00,'2024-03-01',200.00,'Доплата за стаж'),(2,2,202,4500.00,'2024-03-02',150.00,'Допомога по інвалідності'),(3,3,203,6000.00,'2024-03-03',300.00,'Доплата за вислугу років'),(4,4,204,4000.00,'2024-03-04',100.00,'Соціальна виплата'),(5,5,205,5500.00,'2024-03-05',250.00,'Допомога у звязку з втратою годувальника'),(6,6,206,7000.00,'2024-03-06',400.00,'Державна пенсія'),(7,7,207,6500.00,'2024-03-07',350.00,'Чорнобильська доплата');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pensioners`
--

DROP TABLE IF EXISTS `pensioners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pensioners` (
  `pensioner_id` int NOT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `district_code` int DEFAULT NULL,
  `address` text,
  PRIMARY KEY (`pensioner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pensioners`
--

LOCK TABLES `pensioners` WRITE;
/*!40000 ALTER TABLE `pensioners` DISABLE KEYS */;
INSERT INTO `pensioners` VALUES (1,'Іваненко','Іван','Іванович','1950-05-12',101,'вул. Лісова, 10'),(2,'Петренко','Петро','Петрович','1945-08-23',102,'вул. Центральна, 5'),(3,'Сидоренко','Ольга','Михайлівна','1958-03-15',103,'вул. Київська, 7'),(4,'Коваленко','Наталія','Василівна','1952-11-30',104,'вул. Шевченка, 12'),(5,'Мельник','Андрій','Ігорович','1955-07-19',105,'вул. Сонячна, 22'),(6,'Ткаченко','Марія','Федорівна','1949-12-25',106,'вул. Полтавська, 3'),(7,'Григоренко','Олександр','Дмитрович','1953-04-10',107,'вул. Дружби, 8');
/*!40000 ALTER TABLE `pensioners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pensions`
--

DROP TABLE IF EXISTS `pensions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pensions` (
  `pension_code` int NOT NULL,
  `pension_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pension_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pensions`
--

LOCK TABLES `pensions` WRITE;
/*!40000 ALTER TABLE `pensions` DISABLE KEYS */;
INSERT INTO `pensions` VALUES (201,'За віком'),(202,'За інвалідністю'),(203,'За вислугою років'),(204,'Соціальна'),(205,'Втрата годувальника'),(206,'Державна'),(207,'Чорнобильська');
/*!40000 ALTER TABLE `pensions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-03 19:30:23
