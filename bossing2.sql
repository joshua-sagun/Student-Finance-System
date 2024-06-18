-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 02, 2024 at 05:17 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bossing2`
--

-- --------------------------------------------------------

--
-- Table structure for table `phistory`
--

CREATE TABLE `phistory` (
  `payment_id` int(11) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `middlename` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `amount` int(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `usn` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `phistory`
--

INSERT INTO `phistory` (`payment_id`, `firstname`, `middlename`, `lastname`, `amount`, `date`, `usn`) VALUES
(1, 'Aljonnah', 'Marie', 'Tolibas', 2530, '2024-03-02', '21000329000'),
(2, 'Carl', 'Pass', 'Manej', 5000, '2024-03-02', '21000246500'),
(3, 'Carl', 'Pass', 'Manej', 4999, '2024-03-02', '21000246500');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_admin`
--

CREATE TABLE `tbl_admin` (
  `admin_id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_admin`
--

INSERT INTO `tbl_admin` (`admin_id`, `username`, `password`, `name`) VALUES
(1, 'admin1', '123', 'jaredz');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `user_id` int(11) NOT NULL,
  `usn` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `middlename` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `gender` enum('male','female','other') NOT NULL,
  `couryear` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `prelim` int(255) NOT NULL,
  `midterm` int(255) NOT NULL,
  `prefinal` int(255) NOT NULL,
  `final` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_user`
--

INSERT INTO `tbl_user` (`user_id`, `usn`, `password`, `firstname`, `middlename`, `lastname`, `gender`, `couryear`, `address`, `prelim`, `midterm`, `prefinal`, `final`) VALUES
(1, '21000329000', 'test1', 'Aljonnah', 'Marie', 'Tolibas', 'male', 'BSIT-III', 'Butuan Doctors', 6784, 4806, 4806, 3604),
(2, '21000246500', 'test2', 'Carl', 'Pass', 'Manej', 'male', 'BSIT-III', 'Unahan ra', 0, 1591, 4806, 3604);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `phistory`
--
ALTER TABLE `phistory`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `tbl_admin`
--
ALTER TABLE `tbl_admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `tbl_user`
--
ALTER TABLE `tbl_user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `phistory`
--
ALTER TABLE `phistory`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_admin`
--
ALTER TABLE `tbl_admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_user`
--
ALTER TABLE `tbl_user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
