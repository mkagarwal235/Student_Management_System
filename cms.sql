-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 28, 2021 at 02:55 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cms`
--

-- --------------------------------------------------------

--
-- Table structure for table `fee`
--

CREATE TABLE `fee` (
  `receipt_no` varchar(50) NOT NULL,
  `std_name` varchar(100) NOT NULL,
  `admn_no` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `branch` varchar(50) NOT NULL,
  `sem` varchar(50) NOT NULL,
  `paid` int(50) NOT NULL,
  `balance` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fee`
--

INSERT INTO `fee` (`receipt_no`, `std_name`, `admn_no`, `date`, `branch`, `sem`, `paid`, `balance`) VALUES
('123', 'monu kumar', '2018', '2021-06-22', 'BCA', 'sixth', 36800, 0);

-- --------------------------------------------------------

--
-- Table structure for table `library`
--

CREATE TABLE `library` (
  `member_type` varchar(50) NOT NULL,
  `reference_no` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `post_code` int(50) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `book_id` varchar(20) NOT NULL,
  `book_title` text NOT NULL,
  `author` text NOT NULL,
  `date_borrowed` varchar(50) NOT NULL,
  `date_due` varchar(50) NOT NULL,
  `day_in_loan` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `library`
--

INSERT INTO `library` (`member_type`, `reference_no`, `first_name`, `last_name`, `address`, `post_code`, `mobile`, `book_id`, `book_title`, `author`, `date_borrowed`, `date_due`, `day_in_loan`) VALUES
('Student', '2018', 'monu', 'kumar', 'ranchi', 834009, '9162188924', 'ISBN 564524', 'Python Programming', 'John Zelle', '2021-06-22', '2021-07-05', '13');

-- --------------------------------------------------------

--
-- Table structure for table `marksheet`
--

CREATE TABLE `marksheet` (
  `name` varchar(50) NOT NULL,
  `father_name` varchar(50) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `school_name` varchar(20) NOT NULL,
  `roll_no` varchar(10) NOT NULL,
  `mother_name` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `email` varchar(20) NOT NULL,
  `maths` varchar(50) NOT NULL,
  `phy` varchar(50) NOT NULL,
  `chem` varchar(100) NOT NULL,
  `programming` varchar(50) NOT NULL,
  `eng` varchar(50) NOT NULL,
  `grand_total` varchar(50) NOT NULL,
  `cpga` varchar(50) NOT NULL,
  `result` varchar(50) NOT NULL,
  `grade` varchar(100) NOT NULL,
  `percentage` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `marksheet`
--

INSERT INTO `marksheet` (`name`, `father_name`, `dob`, `school_name`, `roll_no`, `mother_name`, `gender`, `email`, `maths`, `phy`, `chem`, `programming`, `eng`, `grand_total`, `cpga`, `result`, `grade`, `percentage`) VALUES
('monu kumar', 'arun agarwal', '04/10/1998', 'CPS', '29', 'anju agarwal', 'Male', 'mka235@gmail.com', '84', '80', '75', '81', '70', '390', '8.2', 'Pass', 'C', '78');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `name` varchar(50) NOT NULL,
  `father_name` varchar(50) NOT NULL,
  `mother_name` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `gender` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`name`, `father_name`, `mother_name`, `address`, `mobile`, `email`, `dob`, `gender`) VALUES
('monu kumar', 'arun agarwal', 'anju agarwal', 'ranchi jhr', '9162188924', 'mka@gmail.com', '04/10/2000', 'Male');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
