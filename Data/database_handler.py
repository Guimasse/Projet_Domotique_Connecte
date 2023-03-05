import os
import mysql.connector as MC
import time


print("Starting !")
for i in range (5):
	print('========')
	#time.sleep(1)

class DatabaseHandler():
	def __init__(self):
		try:
			self.conn = MC.connect(host = '192.168.1.38', database = 'datatest', user = 'root', password = '')
			cursor = self.conn.cursor()
		except MC.Error as err:
			print(err)
			while True:
				choix = input("Tapez 'e' pour quitter !")
				if choix == 'e':
					exit()
		finally:
			if(self.conn.is_connected()):
				print("connected")

	def create_person(self, username: str, password: str):
		cursor = self.conn.cursor()
		req = 'INSERT INTO `person`(`username`, `password`) VALUES (%s,%s);'
		info =(username, password)
		cursor.execute(req, info)
		self.conn.commit()
		cursor.close()

	def password_for(self, username: str):
		cursor = self.conn.cursor()
		req = 'SELECT `password` FROM `person` WHERE `username` = %s;'
		cursor.execute(req, (username,))
		result = cursor.fetchall()
		cursor.close()
		return(format(result[0]))

	def user_exists_with(self, username: str) -> bool:
		cursor = self.conn.cursor()
		req = 'SELECT * FROM `person` WHERE `username` = %s;'
		cursor.execute(req, (username,))
		result = cursor.fetchall()
		cursor.close()

		return len(result) == 1

	def password_edit(self, username: str, password: str):
		cursor =self.conn.cursor()
		req = 'UPDATE `person` SET `password`=%s WHERE `username`=%s;'
		cursor.execute(req, (password, username,))
		self.conn.commit()
		cursor.close()

	def delete_user(self, username:str):
		cursor =self.conn.cursor()
		req = 'DELETE FROM `person` WHERE `username`=%s;'
		cursor.execute(req, (username,))
		self.conn.commit()
		cursor.close()

	def stop(self):
		cursor =self.conn.cursor()
		cursor.close()
		self.conn.close()
		exit();