from tkinter import *

class sensor():
	def add_sensor():
		cnv_sensor_1=Canvas(window, bg='#B9F2FF', highlightthickness=0)
		cnv_title_sensor_1=Canvas(cnv_sensor_1, bg='#69E2FF', highlightthickness=0)

		label_sensor_1 = Label(cnv_title_sensor_1, text="Temperature", font=("Arial", 20), bg='#69E2FF', fg='#1b3646')
		label_sensor_1.pack(side=TOP,pady=10,padx=10)

		cnv_title_sensor_1.pack(side=TOP,fill=X)

		#Fonctiun entry value
		def getentry_sensor_1():
			value_sensor_1 = E1.get()
			Var_S_1.set('Valeur Capteur : ' + str(value_sensor_1))
			print(value_sensor_1)

		Var_S_1 = StringVar()
		label_resultat = Label(cnv_sensor_1, textvariable = Var_S_1, fg='#000731', bg='#D0F6FF', font=("Arial", 15, "bold"))
		label_resultat.pack(side=TOP,fill=X)
		Var_S_1.set('Valeur Capteur : ' + "0.0")

		#ajout bouton
		button=Button(cnv_sensor_1, text="Actualiser",font=("Arial", 15), bg='#DBDBDB', fg='#000731', command=getentry_sensor_1,relief="flat")
		button.pack(side=TOP,fill=X)

		E1 = Entry(cnv_sensor_1, font=("Arial", 15, "bold"),relief="flat")
		E1.pack(side=TOP,fill=X)

		cnv_sensor_1.pack(side=LEFT,fill=Y)

		#separation
		cnv_seperate_1to2=Canvas(window, bg='#D0F6FF', highlightthickness=0, width=2)
		cnv_seperate_1to2.pack(side=LEFT,fill=Y)