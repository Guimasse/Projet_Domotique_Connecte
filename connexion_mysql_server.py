import mysql.connector as MC
from Data.database_handler import DatabaseHandler

class DatabaseHandler():
	def __init__(self, database_name : str):
		conn = MC.connect(host = 'localhost', database = database_name, user = 'root', password = '')
		cursor = conn.cursor()

	def create_person(self, username: str, password: str):
		req = 'INSERT INTO `person`(`username`, `password`) VALUES (%s,%s);'
		info =(username, password)
		cursor.execute(req, info)
		conn.commit()

	def password_for(self, username: str):
		cursor = conn.cursor()
		req = f"SELECT password FROM Person WHERE username = ?;"
		cursor.execute(req, (username,))
		result = cursor.fetchall()
		cursor.close()
		return dict(result[0])["password"]

	def user_exists_with(self, username: str) -> bool:
		cursor = conn.cursor()
		req = f"SELECT * FROM Person WHERE username = ?;"
		cursor.execute(req, (username,))
		result = cursor.fetchall()
		cursor.close()

		return len(result) == 1

try :
	conn = MC.connect(host = 'localhost', database = 'datatest', user = 'root', password = '')
	cursor = conn.cursor()

	print("---Register---")
	username = input("Username : ")
	password = input("Mot de passe : ")



	req = 'INSERT INTO `person`(`username`, `password`) VALUES (%s,%s);'
	info =(username, password)

	cursor.execute(req, info)
	conn.commit()

	req = 'SELECT * FROM person'
	cursor.execute(req)

	personlist = cursor.fetchall()

	for i in personlist:
		print('Prénom : {}'.format(i[0]))
		print('Mdp : {}'.format(i[1]))

finally:
	cursor.close()
	conn.close()