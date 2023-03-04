import mysql.connector as MC

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