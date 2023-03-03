from Data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("database.db")

def register():
	print("---Register---")
	username = input("Username : ")
	password = input("Mot de passe : ")

	database_handler.create_person(username, password)

def login():
	print("---Login---")
	username = input("Username : ")
	password = input("Mot de passe : ")

	if database_handler.user_exists_with(username) and password == database_handler.password_for(username):
		#menu_connected()
		print("login")
	else:
		print("Nom d'utilisateur/mot de passe incorrect.")

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