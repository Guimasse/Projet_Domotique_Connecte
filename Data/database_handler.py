import os
import sqlite3

class DatabaseHandler():
	def _init_(self, database_name : str):
		self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
		self.con.row_factory = sqlite3.Row

	def create_person(self, username: str, password: str):
		cursor = self.con.cursor()
		query = f"INSERT INTO Person (username, password) VALUES (?, ?);"
		cursor.execute(query, (username, password,))
		cursor.close()
		self.con.commit()

	def password_for(self, username: str):
		cursor = self.con.cursor()
		query = f"SELECT password FROM Person WHERE username = ?;"
		cursor.execute(query, (username,))
		result = cursor.fetchall()
		print(result)
		print(result[0])
		print(dict(result[0]))