import sqlite3
from sqlite3 import Error
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    conn.commit()
    conn.close()
 
def create_table(db_file):
	db = sqlite3.connect(db_file)
	cursor = db.cursor()
	cursor.execute('''DROP TABLE IF EXISTS min_max;''')
	cursor.execute('''
	    CREATE TABLE min_max(id INTEGER PRIMARY KEY, value INTEGER)
	''')
	db.commit()
	
# 0 for min
# 1 for max
def insert_value(db_file, min_or_max, input_value):
	db = sqlite3.connect(db_file)
	cursor = db.cursor()
	cursor.execute('''INSERT INTO min_max(id, value)
	                  VALUES(?,?)''', (min_or_max, input_value))
	db.commit()

def init_db(db_file):
	create_connection(db_file)
	create_table(db_file)
	insert_value(db_file, 0, 30)
	insert_value(db_file, 1, 70)

def update_value(db_file, min_or_max, input_value):
	db = sqlite3.connect(db_file)
	cursor = db.cursor()
	cursor.execute('''UPDATE min_max SET value = ? WHERE id = ? ''',
		(input_value, min_or_max))
	db.commit()

def retrieve_data(db_file, min_or_max):
	db = sqlite3.connect(db_file)
	cursor = db.cursor()
	cursor.execute('''SELECT value FROM min_max WHERE id = ? ''',
		(min_or_max,))
	res = cursor.fetchone()[0]
	return res

	
