from Data.database_handler import DatabaseHandler

database_handler = DatabaseHandler()

def register():
	print("---Register---")
	username = input("Username : ")
	password = input("Mot de passe : ")

	database_handler.create_person(username, password)

def modif():
	print("---Edit---")
	username = input("Username : ")
	password = input("Mot de passe a modifier : ")

	database_handler.password_edit(username, password)


def login():
	print("---Login---")
	username = input("Username : ")
	password = input("Mot de passe : ")
	verif = "('"+password+"',)"

	if database_handler.user_exists_with(username) and verif == database_handler.password_for(username):
		#menu_connected()
		print("login")
	else:
		print("Nom d'utilisateur/mot de passe incorrect.")
		print(database_handler.password_for(username))

def menu_not_connect():
	while True:
		print("Bienvenue !")
		print("Choisissez une option")
		print("1. Login")
		print("2. Register")
		print("3. Edit")
		print("4. Exit")
		choix = int(input())

		if choix == 1:
			login()

		if choix == 2:
			register()

		if choix == 3:
			modif()
		if choix == 4:
			database_handler.stop()

menu_not_connect()