CREATE DATABASE Project DEFAULT CHARACTER SET utf8;
USE Project;

INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('Lahore','New York','2019-10-25', 1500, 1700, 55000);
INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('London','New Delhi','2019-10-25', 1000, 1800, 60000);
INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('Karachi','Dubai','2019-10-25', 1200, 1500, 70000);
INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('Dubai','Lahore','2019-10-25', 1600, 2200, 75000);
INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('Karachi','New York','2019-10-25', 1300, 1900, 60000);
INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('Lahore','Manchester','2019-10-25', 1600, 1800, 45000);
INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('Dubai','London','2019-10-25', 1700, 1900, 50000);
INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('New Delhi','New York','2019-10-25', 1500, 1800, 55000);
INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('London','Riyadh','2019-10-25', 0800, 1900, 60000);
INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('Riyadh','Dubai','2019-10-25', 0900, 1400, 90000);
INSERT INTO Flights(Departure, Arrival, YMD, D_Time, A_Time, Fare) VALUES('Lahore','Riyadh','2019-10-25', 0600, 1300, 85000);

INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Momina','03004259404','352021632448','Valencia', 'Pakistani');
INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Iqra','03004259404','352021632448','Gulberg', 'Pakistani');
INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Ahsan','03004259404','352021632448','Defence', 'Pakistani');
INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Hamza','03004259404','352021632448','Iqbal Town', 'Pakistani');
INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Zuwi','03004259404','352021632448','Garden Town', 'Pakistani');
INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Razi','03004259404','352021632448','Model Town', 'Pakistani');
INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Arshad','03004259404','352021632448','American', 'Pakistani');
INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Komal','03004259404','352021632448','Bahria Town', 'Pakistani');
INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Farina','03004259404','352021632448','Defence', 'Pakistani');
INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Zoha','03004259404','352021632448','Model Town', 'Pakistani');
INSERT INTO Passengers(name,phone,cnic,address, nationality) VALUES('Arshad','03004259404','352021632448','Valencia', 'Pakistani');

INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(1,'Lahore','New York');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(2,'New Delhi','New York');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(3,'Riyadh','Dubai');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(4,'Lahore','Manchester');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(2,'Dubai','Lahore');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(3,'Karachi','Dubai');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(2,'London','New Delhi');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(1,'Riyadh','Dubai');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(1,'London','Riyadh');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(5,'Lahore','Riyadh');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(7,'Karachi','New York');
INSERT INTO Tickets(Passenger_ID,Departure,Arrival) VALUES(8,'London','New Delhi');

