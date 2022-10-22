import sqlite3

connection_obj = sqlite3.connect('account1.db')

cursor_obj = connection_obj.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

table = """ CREATE TABLE Account1 (
            user_name text,
            password text,
            Full_name text,
            Email text
		); """

cursor_obj.execute(table)

print("Table is Ready")

connection_obj.close()
