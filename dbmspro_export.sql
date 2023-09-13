-- MySQL dump 10.13  Distrib 5.5.57, for Win64 (AMD64)
--
-- Host: localhost    Database: dbmspro
-- ------------------------------------------------------
-- Server version	5.5.57

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointments` (
  `appointment_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id3` varchar(30) NOT NULL,
  `appointment_date` datetime NOT NULL,
  `appointment_reason` varchar(255) DEFAULT NULL,
  `appointment_notes` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`appointment_id`),
  KEY `patient_id3` (`patient_id3`),
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`patient_id3`) REFERENCES `patients` (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (36,'1001','2022-08-05 13:30:00','Follow-up appointment after surgery','Patient experiencing mild pain and swelling'),(37,'1002','2022-09-12 09:00:00','Routine checkup','Patient has no specific concerns'),(38,'1003','2022-10-20 15:45:00','Chemotherapy session','Patient scheduled for third cycle of chemotherapy'),(39,'1004','2022-11-02 11:30:00','Post-treatment evaluation','Doctor will assess treatment response and discuss next steps'),(40,'1005','2022-09-05 11:15:00','Follow-up appointment after radiation therapy','Patient reported mild skin irritation'),(41,'1006','2022-08-10 13:30:00','Initial consultation for breast cancer','Doctor ordered biopsy for further diagnosis'),(42,'1007','2022-11-15 10:30:00','Follow-up appointment after chemotherapy','Patient experiencing hair loss and fatigue'),(43,'1008','2022-12-20 14:15:00','Consultation for treatment options','Doctor discussed the benefits and risks of radiation therapy'),(46,'1010','2023-05-15 13:30:00','Routine checkup','Doctor will discuss about surgery.'),(47,'1030','2023-09-08 12:30:00','docotor follow up','Recomonded for surgery');
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `d1`
--

DROP TABLE IF EXISTS `d1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `d1` (
  `diagnosis_id1` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` varchar(30) DEFAULT NULL,
  `stage` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`diagnosis_id1`),
  UNIQUE KEY `patient_id` (`patient_id`),
  KEY `stage` (`stage`),
  CONSTRAINT `d1_ibfk_1` FOREIGN KEY (`stage`) REFERENCES `diagnosis1` (`stage`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `d1`
--

LOCK TABLES `d1` WRITE;
/*!40000 ALTER TABLE `d1` DISABLE KEYS */;
INSERT INTO `d1` VALUES (2,'1001','2'),(3,'1002','1');
/*!40000 ALTER TABLE `d1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnosis`
--

DROP TABLE IF EXISTS `diagnosis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagnosis` (
  `diagnosis_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id1` varchar(20) DEFAULT NULL,
  `stage` varchar(10) DEFAULT NULL,
  `diagnosis_date` date DEFAULT NULL,
  PRIMARY KEY (`diagnosis_id`),
  UNIQUE KEY `patient_id1` (`patient_id1`),
  KEY `stage` (`stage`),
  CONSTRAINT `diagnosis_ibfk_1` FOREIGN KEY (`patient_id1`) REFERENCES `patients` (`patient_id`),
  CONSTRAINT `diagnosis_ibfk_2` FOREIGN KEY (`stage`) REFERENCES `diagnosis1` (`stage`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnosis`
--

LOCK TABLES `diagnosis` WRITE;
/*!40000 ALTER TABLE `diagnosis` DISABLE KEYS */;
INSERT INTO `diagnosis` VALUES (114,'1001','1','2022-03-15'),(115,'1002','2','2022-02-10'),(116,'1003','3','2022-01-05'),(117,'1004','2','2021-12-01'),(118,'1005','1','2021-11-15'),(119,'1006','3','2022-04-01'),(120,'1007','1','2022-05-20'),(121,'1008','3','2022-06-15'),(123,NULL,NULL,NULL),(124,NULL,NULL,NULL),(125,NULL,NULL,NULL);
/*!40000 ALTER TABLE `diagnosis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnosis1`
--

DROP TABLE IF EXISTS `diagnosis1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagnosis1` (
  `stage` varchar(10) NOT NULL,
  `cancer_type` varchar(50) DEFAULT NULL,
  `hormone_receptor_status` varchar(50) DEFAULT NULL,
  `her2_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnosis1`
--

LOCK TABLES `diagnosis1` WRITE;
/*!40000 ALTER TABLE `diagnosis1` DISABLE KEYS */;
INSERT INTO `diagnosis1` VALUES ('1','Invasive Lobular Carcinoma','ER/PR-positive','HER2-negative'),('2','Invasive Ductal Carcinoma','ER/PR-positive','HER2-negative'),('2A','HER2-positive Breast Cancer','ER/PR-negative','HER2-positive'),('3','Triple-negative Breast Cancer','ER-negative/PR-negative','HER2-negative');
/*!40000 ALTER TABLE `diagnosis1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnosis3`
--

DROP TABLE IF EXISTS `diagnosis3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagnosis3` (
  `diagnosis_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` varchar(20) DEFAULT NULL,
  `stage` varchar(10) DEFAULT NULL,
  `cancer_type` varchar(50) DEFAULT NULL,
  `hormone_receptor_status` varchar(50) DEFAULT NULL,
  `her2_status` varchar(50) DEFAULT NULL,
  `diagnosis_date` date DEFAULT NULL,
  PRIMARY KEY (`diagnosis_id`),
  UNIQUE KEY `patient_id` (`patient_id`),
  KEY `stage` (`stage`),
  CONSTRAINT `diagnosis3_ibfk_1` FOREIGN KEY (`stage`) REFERENCES `treatments` (`stage`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnosis3`
--

LOCK TABLES `diagnosis3` WRITE;
/*!40000 ALTER TABLE `diagnosis3` DISABLE KEYS */;
INSERT INTO `diagnosis3` VALUES (8,'1001','2','Invasive Ductal Carcinoma','ER/PR-positive','HER2-negative','2022-03-15'),(9,'1002','1','Invasive Lobular Carcinoma','ER/PR-positive','HER2-negative','2022-02-10'),(10,'1003','3','Triple-negative Breast Cancer','ER-negative/PR-negative','HER2-negative','2022-01-05'),(11,'1004','1','Ductal Carcinoma in Situ','ER/PR-positive','HER2-negative','2021-12-01'),(12,'1005','2','HER2-positive Breast Cancer','ER/PR-negative','HER2-positive','2021-11-15'),(13,'1006','3','Triple-negative Breast Cancer','ER-negative/PR-negative','HER2-negative','2022-04-01'),(14,'1007','1','Invasive Ductal Carcinoma','ER/PR-positive','HER2-negative','2022-05-20'),(19,'1010','1','Invasive Lobular Carcinoma','ER/PR-positive','HER2-negative','2023-05-08'),(20,'1030','1','Invasive Lobular Carcinoma','ER/PR-positive','HER2-negative','2023-09-08');
/*!40000 ALTER TABLE `diagnosis3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `diagnosis_p`
--

DROP TABLE IF EXISTS `diagnosis_p`;
/*!50001 DROP VIEW IF EXISTS `diagnosis_p`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `diagnosis_p` (
  `diagnosis_id1` tinyint NOT NULL,
  `patient_id` tinyint NOT NULL,
  `stage` tinyint NOT NULL,
  `cancer_type` tinyint NOT NULL,
  `hormone_receptor_status` tinyint NOT NULL,
  `her2_status` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `empt`
--

DROP TABLE IF EXISTS `empt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empt` (
  `emp` int(11) NOT NULL DEFAULT '0',
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`emp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empt`
--

LOCK TABLES `empt` WRITE;
/*!40000 ALTER TABLE `empt` DISABLE KEYS */;
/*!40000 ALTER TABLE `empt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patients` (
  `patient_id` varchar(25) NOT NULL,
  `symptoms` varchar(255) DEFAULT NULL,
  `tests` varchar(255) DEFAULT NULL,
  `family_history` varchar(255) DEFAULT NULL,
  `tscore` varchar(5) DEFAULT NULL,
  `nscore` varchar(5) DEFAULT NULL,
  `mscore` varchar(5) DEFAULT NULL,
  `stage` int(11) DEFAULT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES ('1001','Breast lump, fatigue','Mammogram, Biopsy','No family history of breast cancer','2','3','1',1),('1002','Breast pain, nipple discharge','Ultrasound, MRI','Mother had breast cancer','1','2','0',2),('1003','Breast swelling, skin changes','Mammogram, Genetic testing','No family history of breast cancer','3','3','1',3),('1004','Breast asymmetry, no symptoms','Clinical breast exam, Mammogram','No family history of breast cancer','2','2','1',2),('1005','Breast mass, axillary lymph node enlargement','Biopsy, PET-CT scan','Sister had breast cancer','2','3','0',1),('1006','Breast pain, nipple retraction','Mammogram, Ultrasound','No family history of breast cancer','1','1','0',3),('1007','Breast lump, skin dimpling','Mammogram, Biopsy','Mother had breast cancer','2','2','1',1),('1008','Breast pain, nipple discharge','MRI, Genetic testing','No family history of breast cancer','3','3','0',3),('1009','Pain','Mammography','Diabities','1','0','0',NULL),('1010','Pain','Mammography','Blood Pressure','1','0','0',1),('1030','Pain','Mamography','Diabities','1','0','0',1);
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `stage` varchar(30) NOT NULL,
  `tests` varchar(255) DEFAULT NULL,
  `medicines` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`stage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treatment`
--

DROP TABLE IF EXISTS `treatment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `treatment` (
  `treatment_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id2` varchar(30) NOT NULL,
  `surgery_type` varchar(50) DEFAULT NULL,
  `chemotherapy_type` varchar(50) DEFAULT NULL,
  `radiation_therapy_type` varchar(50) DEFAULT NULL,
  `hormone_therapy_type` varchar(50) DEFAULT NULL,
  `targeted_therapy_type` varchar(50) DEFAULT NULL,
  `treatment_start_date` date DEFAULT NULL,
  `treatment_end_date` date DEFAULT NULL,
  PRIMARY KEY (`treatment_id`),
  KEY `patient_id2` (`patient_id2`),
  CONSTRAINT `treatment_ibfk_1` FOREIGN KEY (`patient_id2`) REFERENCES `patients` (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treatment`
--

LOCK TABLES `treatment` WRITE;
/*!40000 ALTER TABLE `treatment` DISABLE KEYS */;
INSERT INTO `treatment` VALUES (11,'1001','Lumpectomy','AC-T','External beam radiation','Tamoxifen',NULL,'2022-04-01','2022-09-01'),(12,'1002','Mastectomy','FEC-D','External beam radiation','Aromatase inhibitors','Trastuzumab','2022-03-01','2022-08-01'),(13,'1003','Mastectomy','AC-T','External beam radiation',NULL,NULL,'2022-02-01','2022-07-01'),(14,'1004','Lumpectomy',NULL,'Brachytherapy','Tamoxifen',NULL,'2022-01-01','2022-06-01'),(15,'1005','Mastectomy','AC-T','External beam radiation',NULL,'Trastuzumab','2021-12-01','2022-05-01'),(16,'1006','Lumpectomy','AC-T','External beam radiation','Tamoxifen',NULL,'2022-06-01','2022-11-01'),(17,'1007','Mastectomy','FEC-D','External beam radiation','Aromatase inhibitors','Trastuzumab','2022-05-01','2022-10-01'),(18,'1008','Lumpectomy','AC-T','Brachytherapy','Tamoxifen',NULL,'2022-07-01','2022-12-01');
/*!40000 ALTER TABLE `treatment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treatments`
--

DROP TABLE IF EXISTS `treatments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `treatments` (
  `stage` varchar(10) NOT NULL DEFAULT '',
  `surgery_type` varchar(50) DEFAULT NULL,
  `chemotherapy_type` varchar(50) DEFAULT NULL,
  `radiation_therapy_type` varchar(50) DEFAULT NULL,
  `hormone_therapy_type` varchar(50) DEFAULT NULL,
  `targeted_therapy_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treatments`
--

LOCK TABLES `treatments` WRITE;
/*!40000 ALTER TABLE `treatments` DISABLE KEYS */;
INSERT INTO `treatments` VALUES ('0','Lumpectomy',NULL,NULL,'Tamoxifen',NULL),('1','Lumpectomy','AC-T','Brachytherapy','Tamoxifen',NULL),('2','Mastectomy','AC-T','Brachytherapy','Tamoxifen',NULL),('3','Mastectomy','FEC-0','External Beam Radiation','Aromatase Inhibitors',NULL),('4','Mastectomy','FEC-0','External Beam Radiation','Aromatase Inhibitors','Trastuzumab');
/*!40000 ALTER TABLE `treatments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo` (
  `first_name` varchar(40) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `age` varchar(3) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `user_name` varchar(30) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `Patientid` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Patientid`)
) ENGINE=InnoDB AUTO_INCREMENT=1011 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
INSERT INTO `userinfo` VALUES ('Anjali','Sharma','34','City hill view','Mumbai','Anjali12','Anju@456',1),('Emma','Johnson','40','123 Main St','New York','emma.johnson','password@123',1001),('Olivia','Smith','42','456 Elm St','Los Angeles','olivia.smith','pass@4256',1002),('Ava','Williams','35','789 Oak St','Chicago','ava.williams','ava@5678',1003),('Sophia','Jones','38','321 Pine St','Houston','sophia.jones','pass@1234',1004),('Isabella','Brown','45','654 Cedar St','Miami','isabella.brown','brown@381',1005),('Aaradhya','Patel','42','Marine Drive','Mumbai','aaradhya.patel','patel@423',1006),('Neha','Sharma','58','Vasant Vihar','Delhi','neha.sharma','pass@1584',1007),('Anaya','Gupta','52','Salt Lake','Kolkata','anaya.gupta','anaya@2344',1008),('Shreya ','Nigam','45','Surya nagar','Agra','Shreya23','Anokhi@23',1009),('Anita','Singh','45','Surya Nagar','Agra','Anita123','Anita@123',1010);
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `diagnosis_p`
--

/*!50001 DROP TABLE IF EXISTS `diagnosis_p`*/;
/*!50001 DROP VIEW IF EXISTS `diagnosis_p`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `diagnosis_p` AS select `d`.`diagnosis_id1` AS `diagnosis_id1`,`d`.`patient_id` AS `patient_id`,`d`.`stage` AS `stage`,`d2`.`cancer_type` AS `cancer_type`,`d2`.`hormone_receptor_status` AS `hormone_receptor_status`,`d2`.`her2_status` AS `her2_status` from (`diagnosis1` `d2` join `d1` `d` on((`d2`.`stage` = `d`.`stage`))) where ((`d`.`patient_id` = '1001') and (`d2`.`stage` = (select `d`.`stage` from `d1` `d` where (`d`.`patient_id` = '1001')))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-13 19:02:07
