import mysql.connector
from prettytable import PrettyTable
from prettytable import from_db_cursor
from time import sleep
from os import system

try:
	db = mysql.connector.connect(
	host = '127.0.0.1',
	user = 'root',
	port = '3306',
	password = 'March1997', #March1997
	)

	if db.is_connected():
		cursor = db.cursor()
		cursor.execute('USE PROJECT;')
		system('cls')
		print('WELCOME!')
		input('')

	Passengers = ''' CREATE TABLE IF NOT EXISTS Passengers (
		  Passenger_ID INTEGER NOT NULL AUTO_INCREMENT,
		  name VARCHAR(50) NOT NULL,
		  phone VARCHAR(11) NOT NULL,
		  cnic VARCHAR(13) NOT NULL,
		  address VARCHAR(50) NOT NULL,
		  nationality VARCHAR(50) NOT NULL,
		  PRIMARY KEY(Passenger_ID)
		  )'''
	Flights = ''' CREATE TABLE IF NOT EXISTS Flights (
		Flight_ID INTEGER NOT NULL AUTO_INCREMENT,
		  Departure VARCHAR(20) NOT NULL,
		  Arrival VARCHAR(20) NOT NULL,
		  YMD DATE NOT NULL,
		  D_Time INTEGER NOT NULL,
		  A_Time INTEGER NOT NULL,
		  Fare INTEGER NOT NULL, 
		  PRIMARY KEY(Flight_ID)
		  )'''
	Tickets = ''' CREATE TABLE IF NOT EXISTS Tickets (
		  Ticket_ID INTEGER NOT NULL AUTO_INCREMENT,
		  Passenger_ID INTEGER NOT NULL,
		  Departure VARCHAR(20) NOT NULL,
		  Arrival VARCHAR(20) NOT NULL,
		  PRIMARY KEY(Ticket_ID),
		  CONSTRAINT FOREIGN KEY(Passenger_ID) REFERENCES Passengers(Passenger_ID) ON DELETE CASCADE ON UPDATE CASCADE
		  )'''

	Tables = [Passengers, Flights, Tickets]
	for Table in Tables:
		cursor.execute(Table)

	ar = 'NULL'
	while True:
		system('cls')
		print('Login\n')
		ar = input('Press 1 For Admin. 0 For Receptionist: ')
		if ar == '1':
			print('Enter Username: Admin')
			adminPwd = 'Admin123'
			a = input('Enter Password: ')
			if adminPwd == a:
				print('\nLogin Successful.')
				input('')
				break
			else:
				print('Incorrect Password')
				print('Please Try Again')
				input('')
		elif ar == '0':
			print('Enter Username: Receptionist')
			recepPwd = 'Recep123'
			a = input('Enter Password: ')
			if recepPwd == a:
				print('\nLogin Successful.')
				input('')
				break
			else:
				print('Incorrect Password')
				print('Please Try Again')
				input('')
		else:
			print('Please Enter 1 or 0')
			input('')
	if ar == '1':
		while True:
			system('cls')
			print('ADMINISTRATOR\n')
			print('1. Add a new flight record.')
			print('2. Update existing flight record.')
			print('3. Cancel a particular flight record.')
			print('4. View all flights landing and taking off for a particular airport on that day.')
			print('5. View every table of the database in tabular form.')
			print('6. Log Out')
			n = input('Enter(1-6): ')
			if n == '1':
				system('cls')
				print('1. Add a new flight record.\n')
				dept = input('Enter Departure Airport: ')
				arr = input('Enter Arrival Airport: ')
				d = input('Enter Date(YYYY-MM-DD): ')
				dtime = input('Enter Departure Time(4 Digits): ')
				atime = input('Enter Arrival Time(4 Digits): ')
				fare = input('Enter Fare: ')
				cursor.execute('INSERT INTO Flights(Departure,Arrival,YMD,D_Time,A_Time, Fare) VALUES (\''+dept+'\',\''+arr+'\',\''+d+'\','+dtime+','+atime+','+fare+')')
				db.commit()
				cursor.execute('SELECT * FROM Flights')
				t = from_db_cursor(cursor)
				print(t)
				input('')
			elif n == '2':
				system('cls')
				print('2. Update existing flight record.\n')
				cursor.execute('SELECT * FROM Flights')
				t = from_db_cursor(cursor)
				print(t)
				x = input('Choose Flight ID to Update: ')
				c = input('Enter 1.Departure Airport, 2.Arrival Airport, 3.Date, 4.Departure Time, 5.Arrival Time, 6.Fare: ')
				if c == '1':
					up = input('Enter New Departure Airport: ')
					cursor.execute('UPDATE Flights SET Departure = \''+up+'\' WHERE Flight_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Flights')
					t = from_db_cursor(cursor)
					print(t)
					input('')
				elif c == '2':
					up = input('Enter New Arrival Airport: ')
					cursor.execute('UPDATE Flights SET Arrival = \''+up+'\' WHERE Flight_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Flights')
					t = from_db_cursor(cursor)
					print(t)
					input('')
				elif c == '3':
					up = input('Enter New Date(YYYY-MM-DD): ')
					cursor.execute('UPDATE Flights SET YMD = \''+up+'\' WHERE Flight_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Flights')
					t = from_db_cursor(cursor)
					print(t)
					input('')
				elif c == '4':
					up = input('Enter New Departure Time: ')
					cursor.execute('UPDATE Flights SET D_Time = '+up+' WHERE Flight_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Flights')
					t = from_db_cursor(cursor)
					print(t)
					input('')
				elif c == '5':
					up = input('Enter New Arrival Time: ')
					cursor.execute('UPDATE Flights SET A_Time = '+up+' WHERE Flight_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Flights')
					t = from_db_cursor(cursor)
					print(t)
					input('')
				elif c == '6':
					up = input('Enter New Fare: ')
					cursor.execute('UPDATE Flights SET Fare = '+up+' WHERE Flight_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Flights')
					t = from_db_cursor(cursor)
					print(t)
					input('')
			elif n == '3':
				system('cls')
				print('3. Cancel a particular flight record.\n')
				cursor.execute('SELECT * FROM Flights')
				t = from_db_cursor(cursor)
				print(t)
				x = input('Choose Flight ID To Cancel: ')
				cursor.execute('DELETE FROM Flights WHERE Flight_ID = '+x+'')
				cursor.execute('SELECT * FROM Flights')
				t = from_db_cursor(cursor)
				print(t)
				input('')
			elif n == '4':
				system('cls')
				print('4. View all flights landing and taking off for a particular airport on that day.\n')
				a = input('Enter Airport: ')
				cursor.execute('SELECT * FROM Flights WHERE Departure = \''+a+'\' OR Arrival = \''+a+'\'')
				t = from_db_cursor(cursor)
				print(t)
				input('')
			elif n=='5':
				system('cls')
				print('5. View every table of the database in tabular form.')
				for t in Tables:
					cursor.execute('SELECT * FROM '+t+'')
					t = from_db_cursor(cursor)
					print(t)
					print('\n')
				input('')
			elif n=='6':
				system('cls')
				print('6. Log Out')
				input('')
				break
	elif ar == '0':
		while True:
			system('cls')
			print('RECEPTIONIST\n')
			print('1. Create a new passenger record.')
			print('2. Update existing passenger record.')
			print('3. Generate ticket record for a particular passenger for a particular flight')
			print('4. Using departure airport IATA code and arrival airport IATA code, view all available flights in a particular time period')
			print('5. Using departure airport IATA code and arrival airport IATA code, view the cheapest flight.')
			print('6. View flight history of a particular passenger.')
			print('7. Cancel a particular ticket record')
			print('8. Log Out')
			n = input('Enter(1-8): ')
			if n=='1':
				system('cls')
				print('1. Create a new passenger record.\n')
				name = input('Enter Name: ')
				ph = input('Enter Phone #: ')
				cn = input('Enter CNIC: ')
				add = input ('Enter Address: ')
				nat = input('Enter Nationality: ')
				cursor.execute('INSERT INTO Passengers(name, phone, cnic, address, nationality) VALUES(\''+name+'\',\''+ph+'\',\''+cn+'\', \''+add+'\', \''+nat+'\')')
				db.commit()
				cursor.execute('SELECT * FROM Passengers')
				t = from_db_cursor(cursor)
				print(t)
				input('')
			elif n=='2':
				system('cls')
				print('2. Update existing passenger record.')
				cursor.execute('SELECT * FROM Passengers')
				t = from_db_cursor(cursor)
				print(t)
				x = input('Choose Passenger ID to Update: ')
				c = input('Enter 1.Name, 2.Phone Number, 3.CNIC, 4.Address, 5.Nationality: ')
				if c == '1':
					up = input('Enter New Name: ')
					cursor.execute('UPDATE Passengers SET name = \''+up+'\' WHERE Passenger_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Passengers')
					t = from_db_cursor(cursor)
					print(t)
					input('')
				elif c == '2':
					up = input('Enter New Phone: ')
					cursor.execute('UPDATE Passengers SET phone = \''+up+'\' WHERE Passenger_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Passengers')
					t = from_db_cursor(cursor)
					print(t)
					input('')
				elif c == '3':
					up = input('Enter New CNIC: ')
					cursor.execute('UPDATE Passengers SET cnic = \''+up+'\' WHERE Passenger_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Passengers')
					t = from_db_cursor(cursor)
					print(t)
					input('')
				elif c == '4':
					up = input('Enter New Address: ')
					cursor.execute('UPDATE Passengers SET address = \''+up+'\' WHERE Passenger_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Passengers')
					t = from_db_cursor(cursor)
					print(t)
					input('')
				elif c == '5':
					up = input('Enter New Nationality: ')
					cursor.execute('UPDATE Passengers SET nationality = \''+up+'\' WHERE Passenger_ID = '+x+'')
					db.commit()
					cursor.execute('SELECT * FROM Passengers')
					t = from_db_cursor(cursor)
					print(t)
					input('')
				input('')
			elif n=='3':
				system('cls')
				print('3. Generate ticket record for a particular passenger for a particular flight')
				cursor.execute('SELECT * FROM Passengers')
				t = from_db_cursor(cursor)
				print(t)
				x = input('Choose a Passenger ID: ')
				cursor.execute('SELECT * FROM Flights')
				t = from_db_cursor(cursor)
				print(t)
				da = input('Enter Departure Airport: ')
				aa = input('Enter Arrival Airport: ')
				cursor.execute('INSERT INTO Tickets(Passenger_ID,Departure, Arrival) VALUES('+x+',\''+da+'\',\''+aa+'\')')
				cursor.execute('SELECT * FROM Tickets')
				t = from_db_cursor(cursor)
				print(t)
				input('')
			elif n=='4':
				system('cls')
				print('4. Using departure airport IATA code and arrival airport IATA code, view all available flights in a particular time period')
				cursor.execute('SELECT * FROM Flights')
				t = from_db_cursor(cursor)
				print(t)
				ap = input('Enter Airport Name: ')
				maxTime = input('Maximum Time: ')
				minTime = input('Minimum Time: ')
				cursor.execute('SELECT * FROM Flights WHERE Departure = \''+ap+'\' OR Arrival = \''+ap+'\' AND D_Time BETWEEN '+maxTime+' and '+minTime+' AND A_Time BETWEEN '+maxTime+' and '+minTime+'')
				t = from_db_cursor(cursor)
				print(t)
				input('')
			elif n=='5':
				system('cls')
				print('5. Using departure airport IATA code and arrival airport IATA code, view the cheapest flight.')
				cursor.execute('SELECT * FROM Flights')
				t = from_db_cursor(cursor)
				print(t)
				ap = input('Enter Airport Name: ')
				cursor.execute('SELECT MIN(Fare) as Min_Fare FROM Flights WHERE  Departure = \''+ap+'\' OR Arrival = \''+ap+'\' LIMIT 1')
				minimum = cursor.fetchall()
				cursor.execute('SELECT * FROM Flights WHERE Fare = '+str(minimum[0][0])+' AND Departure = \''+ap+'\'')
				one = cursor.fetchall()
				cursor.execute('SELECT * FROM Flights WHERE Fare = '+str(minimum[0][0])+' AND Arrival = \''+ap+'\'')
				two = cursor.fetchall()
				if one == []:
					cursor.execute('SELECT * FROM Flights WHERE Fare = '+str(minimum[0][0])+' AND Arrival = \''+ap+'\'')
					t = from_db_cursor(cursor)
					print(t)
				elif two == []:
					cursor.execute('SELECT * FROM Flights WHERE Fare = '+str(minimum[0][0])+' AND Departure = \''+ap+'\'')
					t = from_db_cursor(cursor)
					print(t)
				input('')
			elif n=='6':
				system('cls')
				print('6. View flight history of a particular passenger.')
				cursor.execute('SELECT * FROM Passengers')
				x = input('Choose Passenger ID: ')
				cursor.execute('SELECT * FROM Tickets WHERE Passenger_ID = '+x+'')
				t = from_db_cursor(cursor)
				print(t)
				input('')
			elif n=='7':
				system('cls')
				print('7. Cancel a particular ticket record')
				cursor.execute('SELECT * FROM Tickets')
				t = from_db_cursor(cursor)
				print(t)
				x = input('Choose Ticket ID: ')
				cursor.execute('DELETE FROM Tickets WHERE Ticket_ID = '+x+'')
				cursor.execute('SELECT * FROM Tickets')
				t = from_db_cursor(cursor)
				print(t)
				input('')
			elif n=='8':
				system('cls')
				print('8. Log Out')
				input('')
				break
except Exception as e: 
	print(e)
