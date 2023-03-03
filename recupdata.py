from Data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("database.db")

def register():
	print("---Register---")
	username = input("Username : ")
	password = input("Mot de passe : ")

	database_handler.create_person(username, password)

def menu_not_connect():
	while True:
		print("Bienvenue !")
		print("Choisissez une option")
		print("1. Login")
		print("2. Register")
		choix = int(input())

		if choix == 1:
			login()
		if choix == 2:
			register()

menu_not_connect()