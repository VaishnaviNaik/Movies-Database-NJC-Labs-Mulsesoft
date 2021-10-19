import sqlite3


#Creating connection to an existing database or create new database if it does not exist
conn = sqlite3.connect('movie_management.db')

#Creating cursor to interact with the database 
c = conn.cursor()

#Creating Table

c.execute(""" CREATE TABLE Movies(
	id INTEGER PRIMARY KEY,
	Movie_Name TEXT,
	Lead_Actor TEXT,
	Actress TEXT,
	Director TEXT,
	Year_of_Release INTEGER
	) 
	""")


#Inserting single record into table
c.execute("INSERT INTO Movies VALUES(1,'Midsommar','Jack Reynor','Florence Pugh','Ari Aster',2019)")

#To insert multiple records at once
many_movies = [ 
				(2,'The Matrix','Keanu Reeves','Carrie-Anne Moss','The Wachowskis',1999),
				(3,'Interstellar','Matthew McConaughey','Anne Hathaway','Christopher Nolan',2014),	
				(4,'The Godfather','Marlon Brando','Diane Keaton','Francis Ford Coppola',1972),
				(5,'Train to Busan','Gong Yoo','Kim Su An','Yeon Sang-ho',2016),
				(6,'Constantine','Keanu Reeves','Rachel Weisz','Francis Lawrence',2005)
			  ]

#Using '?' as placeholder and executemany command to insert multiple records at once
c.executemany("INSERT INTO Movies VALUES(?,?,?,?,?,?)", many_movies)


print("\nData Contained in Movies Table:\n")

c.execute("SELECT * FROM Movies")

items = c.fetchall()
for item in items:
	#Converting integer to string to use for concatenation 
	print(str(item[0])+" | "+item[1]+" | "+item[2]+" | "+item[3]+" | "+item[4]+" | "+str(item[5]))


print("\n\nMovies where Keanu Reeves is the lead actor:\n")


c.execute("SELECT Movie_Name FROM Movies WHERE Lead_Actor = 'Keanu Reeves'")

movie_names = c.fetchall()
for name in movie_names:
	print(name[0])

conn.commit()
conn.close()
