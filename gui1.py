from tkinter import*
from PIL import Image, ImageTk

window = Tk()
window.title("Welcome")
window.resizable(0,0)

name = StringVar()

def ole():
    nombre = entry1.get()
    country = var.get()
    welcoming = "Hello "+nombre+" from "+country
    label_resumen["text"] = welcoming


def game():
    import intentodejuego
    open(intentodejuego)

imge = Image.open("C:/Users/sergi/Desktop/snakelogo2.jpg")
photo = ImageTk.PhotoImage(imge)

lab0 = Label(image=photo, width=800, bg="light green")
lab0.grid()

labsnake = Label(master=window, text="SNAKE", width=47, font=("Calibri",25, "bold"), fg="green", bg="light green")
labsnake.grid(row=1, column=0)

lab1 = Label(master=window, text="Name > > >", width=21, font=("Calibri", 20, "bold"), fg="green", bg="light green")
lab1.grid(row=2, column=0, sticky="w")

entry1 = Entry(window, textvar=name, bg="light green")
entry1.grid(row=2, column=0)

lab2 = Label(master=window, text=" < < < Name", width=21, font=("Calibri", 20, "bold"), fg="green", bg="light green")
lab2.grid(row=2, column=0, sticky="e")

lab3 = Label(master=window, text="Country > > >", width=21, font=("Calibri", 20, "bold"), fg="green", bg="light green")
lab3.grid(row=3, column=0, sticky="w")

var = StringVar()
list1 = ["Argentina", "Spain", "Venezuela", "Italy", "Portugal", "USA", "France", "Morocco", "Egypt", "Kazakhstan", "Lebanon", "Romania", "Belgium"]
droplist = OptionMenu(window, var, *list1)
var.set("Select BIS nationality")
droplist.config(width=20, bg="light green")
droplist.grid(row=3, column=0)

lab4 = Label(master=window, text=" < < < Country", width=21, font=("Calibri", 20, "bold"), fg="green", bg="light green")
lab4.grid(row=3, column=0, sticky="e")

lab5 = Label(master=window, text="What do you want to do?", width=47, font=("Calibri", 25, "bold"), fg="green", bg="light green")
lab5.grid(row=4, column=0)

label_resumen = Label(master=window, width=47, font=("Calibri", 25, "bold"), fg="green", bg="light green")
label_resumen.grid(row=6, column=0)

bt1 = Button(master=window, text="Play", width=25, font=("Arial", 15, "bold"), fg="green", bg="light green", command=game)
bt1.grid(row=5, column=0, sticky="w")

bt3 = Button(master=window, text="Welcome", width=25, font=("Arial", 15, "bold"), fg="green", bg="light green", command=ole)
bt3.grid(row=5, column=0)

bt2 = Button(master=window, text="Exit", width=25, font=("Arial", 15, "bold"), fg="green", bg="light green", command=sys.exit)
bt2.grid(row=5, column=0, sticky="e")

window.mainloop()