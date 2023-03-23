from tkinter import *
import webbrowser

def open_youtube():
	webbrowser.open_new("https://www.youtube.com/")

# crer premiere fenetre
window = Tk()

window.title("IHM")
window.geometry("720x480")
window.minsize(720,480)
window.iconbitmap("icon.ico")
window.config(background='#D0F6FF')

#ajouter titre
can_title=Canvas(window, bg='#99EBFF', highlightthickness=0)
frame_title=Frame(can_title, bg='#99EBFF')

label_title = Label(frame_title, text="IHM Domotique", font=("Arial", 30, "bold"), bg='#99EBFF', fg='#1b3646')
label_title.pack(side=LEFT)
label_under_title = Label(frame_title, text="[Test Intergace Graphique]", font=("Arial", 20, "bold"), bg='#99EBFF', fg='#1b3646')
label_under_title.pack(side=LEFT)

frame_title.pack(side=LEFT,padx=30)
can_title.pack(side=TOP,fill=X)

#add first sensor
cnv_first_sensor=Canvas(window, bg='#B9F2FF', highlightthickness=0)
cnv_title_sensor_1=Canvas(cnv_first_sensor, bg='#69E2FF', highlightthickness=0)


label_first_sensor = Label(cnv_title_sensor_1, text="Temperature", font=("Arial", 20), bg='#69E2FF', fg='#1b3646')
label_first_sensor.pack(side=TOP,pady=10,padx=10)

cnv_title_sensor_1.pack(side=TOP,fill=X)

#separation
cnv_seperate_top=Canvas(window, bg='#D0F6FF', highlightthickness=0, height=2)
cnv_seperate_top.pack(side=TOP,fill=X)

#ajout 2e bouton
button=Button(cnv_first_sensor, text="Ouvrir Youtube",font=("Arial", 15, "bold"), bg='#DBDBDB', fg='#000731', command=open_youtube,relief="flat")
button.pack(side=TOP,pady=30,fill=X)

cnv_first_sensor.pack(side=LEFT,fill=Y)

#separation
cnv_seperate_1to2=Canvas(window, bg='#D0F6FF', highlightthickness=0, width=2)
cnv_seperate_1to2.pack(side=LEFT,fill=Y)

#add first sensor
cnv_sensor_2=Canvas(window, bg='#B9F2FF', highlightthickness=0)
cnv_title_sensor_2=Canvas(cnv_sensor_2, bg='#69E2FF', highlightthickness=0)


label_sensor_2 = Label(cnv_title_sensor_2, text="Humidité", font=("Arial", 20), bg='#69E2FF', fg='#1b3646')
label_sensor_2.pack(side=TOP,pady=10,padx=10)

cnv_title_sensor_2.pack(side=TOP,fill=X)

#ajout bouton
button=Button(cnv_sensor_2, text="Ouvrir Youtube",font=("Arial", 15, "bold"), bg='#DBDBDB', fg='#000731', command=open_youtube,relief="flat")
button.pack(side=TOP,pady=30,fill=X)

cnv_sensor_2.pack(side=LEFT,fill=Y)

#separation
cnv_seperate_2to3=Canvas(window, bg='#D0F6FF', highlightthickness=0, width=2)
cnv_seperate_2to3.pack(side=LEFT,fill=Y)

#add first sensor
cnv_sensor_3=Canvas(window, bg='#B9F2FF', highlightthickness=0)
cnv_title_sensor_3=Canvas(cnv_sensor_3, bg='#69E2FF', highlightthickness=0)


label_sensor_3 = Label(cnv_title_sensor_3, text="Niveau", font=("Arial", 20), bg='#69E2FF', fg='#1b3646')
label_sensor_3.pack(side=TOP,pady=10,padx=10)

cnv_title_sensor_3.pack(side=TOP,fill=X)

#ajout bouton
button=Button(cnv_sensor_3, text="Ouvrir Youtube",font=("Arial", 15, "bold"), bg='#DBDBDB', fg='#000731', command=open_youtube,relief="flat")
button.pack(side=TOP,pady=30,fill=X)

cnv_sensor_3.pack(side=LEFT,fill=Y)

# affichage
window.mainloop()