# create a SQLite3 table and populate it with data
import sqlite3

# create a new database
with sqlite3.connect("blog.db") as connection:
	# get a cursor object uesd to execute sql commands
	c = connection.cursor()

	# create a new table 
	c.execute("""CREATE TABLE posts 
		(title TEXT, post TEXT)
		""")

	# insert dummy data into posts
	c.execute("INSERT INTO posts VALUES('good', 'hhhhhh,goooood!')")
	c.execute("INSERT INTO posts VALUES('well', 'well down!')")
	c.execute("INSERT INTO posts VALUES('excellent', 'wow, excellent!')")
	c.execute('INSERT INTO posts VALUES("okey", "oh, i\'m okey.")')
