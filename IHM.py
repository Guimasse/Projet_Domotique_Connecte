from tkinter import *
import tkinter.font as tkFont
from PIL import ImageFont
import webbrowser

nb = 5.00
value_sensor_2=0

def open_youtube():
	webbrowser.open_new("https://www.youtube.com/")

def add_sensor_temp():

	cnv_sensor_1=Canvas(window, bg='#B9F2FF', width=500,highlightthickness=0)
	cnv_title_sensor_1=Canvas(cnv_sensor_1, bg='#69E2FF', highlightthickness=0)

	label_sensor_1 = Label(cnv_title_sensor_1, text="Temperature", font=("Arial", 20), bg='#69E2FF', fg='#1b3646')
	label_sensor_1.pack(side=TOP,pady=10,padx=10)

	cnv_title_sensor_1.pack(side=TOP,fill=X)

	#Fonctiun entry value
	def getentry_sensor_1():
		value_sensor_1 = E1.get()
		Var_S_1.set(str(value_sensor_1)+"°C")
		print(value_sensor_1)

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

	#Fonctiun entry value
	def getentry_sensor_2():
		global value_sensor_2
		value_sensor_2 = E2.get()
		Var_S_2.set(str(value_sensor_2))
		if int(value_sensor_2)==7:
			cnv_level_1.itemconfig(level7, fill='green')
			cnv_level_1.itemconfig(level6, fill='green')
			cnv_level_1.itemconfig(level5, fill='green')
			cnv_level_1.itemconfig(level4, fill='green')
			cnv_level_1.itemconfig(level3, fill='green')
			cnv_level_1.itemconfig(level2, fill='green')
			cnv_level_1.itemconfig(level1, fill='green')
			cnv_level_1.itemconfig(level0, fill='gray')
		if int(value_sensor_2)==6:
			cnv_level_1.itemconfig(level7, fill='gray')
			cnv_level_1.itemconfig(level6, fill='green')
			cnv_level_1.itemconfig(level5, fill='green')
			cnv_level_1.itemconfig(level4, fill='green')
			cnv_level_1.itemconfig(level3, fill='green')
			cnv_level_1.itemconfig(level2, fill='green')
			cnv_level_1.itemconfig(level1, fill='green')
			cnv_level_1.itemconfig(level0, fill='gray')
		if int(value_sensor_2)==5:
			cnv_level_1.itemconfig(level7, fill='gray')
			cnv_level_1.itemconfig(level6, fill='gray')
			cnv_level_1.itemconfig(level5, fill='green')
			cnv_level_1.itemconfig(level4, fill='green')
			cnv_level_1.itemconfig(level3, fill='green')
			cnv_level_1.itemconfig(level2, fill='green')
			cnv_level_1.itemconfig(level1, fill='green')
			cnv_level_1.itemconfig(level0, fill='gray')
		if int(value_sensor_2)==4:
			cnv_level_1.itemconfig(level7, fill='gray')
			cnv_level_1.itemconfig(level6, fill='gray')
			cnv_level_1.itemconfig(level5, fill='gray')
			cnv_level_1.itemconfig(level4, fill='green')
			cnv_level_1.itemconfig(level3, fill='green')
			cnv_level_1.itemconfig(level2, fill='green')
			cnv_level_1.itemconfig(level1, fill='green')
			cnv_level_1.itemconfig(level0, fill='gray')
		if int(value_sensor_2)==3:
			cnv_level_1.itemconfig(level7, fill='gray')
			cnv_level_1.itemconfig(level6, fill='gray')
			cnv_level_1.itemconfig(level5, fill='gray')
			cnv_level_1.itemconfig(level4, fill='gray')
			cnv_level_1.itemconfig(level3, fill='green')
			cnv_level_1.itemconfig(level2, fill='green')
			cnv_level_1.itemconfig(level1, fill='green')
			cnv_level_1.itemconfig(level0, fill='gray')
		if int(value_sensor_2)==2:
			cnv_level_1.itemconfig(level7, fill='gray')
			cnv_level_1.itemconfig(level6, fill='gray')
			cnv_level_1.itemconfig(level5, fill='gray')
			cnv_level_1.itemconfig(level4, fill='gray')
			cnv_level_1.itemconfig(level3, fill='gray')
			cnv_level_1.itemconfig(level2, fill='green')
			cnv_level_1.itemconfig(level1, fill='green')
			cnv_level_1.itemconfig(level0, fill='gray')
		if int(value_sensor_2)==1:
			cnv_level_1.itemconfig(level7, fill='gray')
			cnv_level_1.itemconfig(level6, fill='gray')
			cnv_level_1.itemconfig(level5, fill='gray')
			cnv_level_1.itemconfig(level4, fill='gray')
			cnv_level_1.itemconfig(level3, fill='gray')
			cnv_level_1.itemconfig(level2, fill='gray')
			cnv_level_1.itemconfig(level1, fill='green')
			cnv_level_1.itemconfig(level0, fill='gray')
		if int(value_sensor_2)==0:
			cnv_level_1.itemconfig(level7, fill='gray')
			cnv_level_1.itemconfig(level6, fill='gray')
			cnv_level_1.itemconfig(level5, fill='gray')
			cnv_level_1.itemconfig(level4, fill='gray')
			cnv_level_1.itemconfig(level3, fill='gray')
			cnv_level_1.itemconfig(level2, fill='gray')
			cnv_level_1.itemconfig(level1, fill='gray')
			cnv_level_1.itemconfig(level0, fill='red')

	Var_S_2 = StringVar()
	label_resultat = Label(cnv_sensor, textvariable = Var_S_2, fg='#000731', bg='#D0F6FF', font=("Seven Segment", 60, "bold"))
	label_resultat.pack(side=TOP,fill=X)
	Var_S_2.set("0")

	#ajout bouton
	button=Button(cnv_sensor, text="Actualiser",font=("Arial", 15), bg='#DBDBDB', fg='#000731', command=getentry_sensor_2,relief="flat")
	button.pack(side=TOP,fill=X)

	E2 = Entry(cnv_sensor, font=("Arial", 15, "bold"),relief="flat")
	E2.pack(side=TOP,fill=X)

	def create_circle(y, x, r, canvas, color): #center coordinates, radius
		x0 = x - r
		y0 = y - r
		x1 = x + r
		y1 = y + r
		if color == 1 :
			return canvas.create_oval(x0, y0, x1, y1, fill='green')
		if color == 0 :
			return canvas.create_oval(x0, y0, x1, y1, fill='gray')
		if color == 2 :
			return canvas.create_oval(x0, y0, x1, y1, fill='red')


	cnv_level=Canvas(cnv_sensor, bg='blue', highlightthickness=0)
	cnv_level_1=Canvas(cnv_level, bg='white', highlightthickness=0, bd=0, height=600, width=400)
	cnv_level_1.pack(fill=X, expand=1)
	coordinatex=200
	level7=create_circle(25, coordinatex, 15, cnv_level_1, 0)
	level6=create_circle(75, coordinatex, 15, cnv_level_1,0)
	level5=create_circle(125, coordinatex, 15, cnv_level_1,0)
	level4=create_circle(175, coordinatex, 15, cnv_level_1,0)
	level3=create_circle(225, coordinatex, 15, cnv_level_1,0)
	level2=create_circle(275, coordinatex, 15, cnv_level_1,0)
	level1=create_circle(325, coordinatex, 15, cnv_level_1,0)
	level0=create_circle(375, coordinatex, 15, cnv_level_1,2)

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