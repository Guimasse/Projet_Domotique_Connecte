from tkinter import *
import webbrowser

nb = 5.00

def open_youtube():
	webbrowser.open_new("https://www.youtube.com/")

def add_sensor_temp():
	cnv_sensor_1=Canvas(window, bg='#B9F2FF', highlightthickness=0)
	cnv_title_sensor_1=Canvas(cnv_sensor_1, bg='#69E2FF', highlightthickness=0)

	label_sensor_1 = Label(cnv_title_sensor_1, text="Temperature", font=("Arial", 20), bg='#69E2FF', fg='#1b3646')
	label_sensor_1.pack(side=TOP,pady=10,padx=10)

	cnv_title_sensor_1.pack(side=TOP,fill=X)

	#Fonctiun entry value
	def getentry_sensor_1():
		value_sensor_1 = E1.get()
		Var_S_1.set(str(value_sensor_1)+"°C")
		print(value_sensor_1)

	#label_title_result = Label(cnv_sensor_1, text ="Valeur Capteur : ", fg='#000731', bg='#D0F6FF', font=("Arial", 15, "bold"))
	#label_title_result.pack(side=TOP,fill=X)

	Var_S_1 = StringVar()
	label_resultat = Label(cnv_sensor_1, textvariable = Var_S_1, fg='#000731', bg='#D0F6FF', font=("Seven Segment", 60, "bold"))
	label_resultat.pack(side=TOP,fill=X)
	Var_S_1.set("0.0"+"°C")

	#ajout bouton
	button=Button(cnv_sensor_1, text="Actualiser",font=("Arial", 15), bg='#DBDBDB', fg='#000731', command=getentry_sensor_1,relief="flat")
	button.pack(side=TOP,fill=X)

	E1 = Entry(cnv_sensor_1, font=("Arial", 15, "bold"),relief="flat")
	E1.pack(side=TOP,fill=X)

	cnv_sensor_1.pack(side=LEFT,fill=Y)

	#separation
	cnv_seperate_1to2=Canvas(window, bg='#D0F6FF', highlightthickness=0, width=2)
	cnv_seperate_1to2.pack(side=LEFT,fill=Y)

def add_sensor_level():

	cnv_sensor=Canvas(window,width=500, bg='#B9F2FF', highlightthickness=0)
	cnv_title_sensor=Canvas(cnv_sensor, bg='#69E2FF', highlightthickness=0)

	label_sensor = Label(cnv_title_sensor, text="Niveau de Cuve (NORD)", font=("Arial", 20), bg='#69E2FF', fg='#1b3646')
	label_sensor.pack(side=TOP,pady=10,padx=10)

	cnv_title_sensor.pack(side=TOP,fill=X)

	Var_S_1 = StringVar()
	label_resultat = Label(cnv_sensor, textvariable = Var_S_1, fg='#000731', bg='#D0F6FF', font=("Seven Segment", 60, "bold"))
	label_resultat.pack(side=TOP,fill=X)
	Var_S_1.set("0")

	cnv_level=Canvas(cnv_sensor, bg='blue', highlightthickness=0)

	def create_circle(y, x, r, canvas, color): #center coordinates, radius
		x0 = x - r
		y0 = y - r
		x1 = x + r
		y1 = y + r
		if color == 1 :
			return canvas.create_oval(x0, y0, x1, y1, fill='green', width=0)

	cnv_level_1=Canvas(cnv_level, bg='white', highlightthickness=0, bd=0, height=600)
	cnv_level_1.pack(fill=X, expand=1)
	coordinatex=175
	create_circle(40, coordinatex, 20, cnv_level_1, 1)
	create_circle(100, coordinatex, 20, cnv_level_1,1)
	create_circle(160, coordinatex, 20, cnv_level_1,1)
	create_circle(220, coordinatex, 20, cnv_level_1,1)
	create_circle(280, coordinatex, 20, cnv_level_1,1)
	create_circle(340, coordinatex, 20, cnv_level_1,1)
	create_circle(400, coordinatex, 20, cnv_level_1,1)
	create_circle(460, coordinatex, 20, cnv_level_1,1)

	cnv_level.pack(side=TOP,fill=X)


	cnv_sensor.pack(side=LEFT,fill=Y)

	#separation
	cnv_seperate=Canvas(window, bg='#D0F6FF', highlightthickness=0, width=2)
	cnv_seperate.pack(side=LEFT,fill=Y)

# crer premiere fenetre
window = Tk()

window.title("IHM")
window.geometry("1280x720")
window.minsize(720,480)
window.iconbitmap("icon.ico")
window.config(background='#D0F6FF')

#======================================================================================================================================================
#																TOP
#======================================================================================================================================================

#ajouter titre
can_title=Canvas(window, bg='#99EBFF', highlightthickness=0)
frame_title=Frame(can_title, bg='#99EBFF')

label_title = Label(frame_title, text="IHM Domotique", font=("Arial", 30, "bold"), bg='#99EBFF', fg='#1b3646')
label_title.pack(side=LEFT)
label_under_title = Label(frame_title, text="[Test Intergace Graphique]", font=("Arial", 20, "bold"), bg='#99EBFF', fg='#1b3646')
label_under_title.pack(side=LEFT)

frame_title.pack(side=LEFT,padx=30)
can_title.pack(side=TOP,fill=X)

cnv_seperate_top=Canvas(window, bg='#D0F6FF', highlightthickness=0, height=2)
cnv_seperate_top.pack(side=TOP,fill=X)

#=======================================================================SENSOR 1===============================================================================

add_sensor_temp()
add_sensor_level()

# affichage
window.mainloop()