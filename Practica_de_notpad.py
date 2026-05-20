from tkinter import *

vent= Tk()
vent.geometry("800x500")

label_file_name= Label(vent,text="Nombre")
label_file_name.place(relx=0.3,rely=0.1,anchor=CENTER)

input_file_name = Entry(vent)
input_file_name.place(relx=0.5,rely=0.1,anchor=CENTER)

my_text= Text(vent,height=5,width=40)
my_text.place(relx=0.5,rely=0.4,anchor=CENTER)

def clearInputFeild():
    input_file_name.delete(0, END)

def clearTextarea():
    my_text.delete(1.0, END)

def addData():
    input_file_name.insert(END,"myfile")
    
open_button=Button(vent,text="borrar campo de entrada",command= clearInputFeild)
open_button.place(relx=0.25,rely=0.7,anchor=CENTER)
save_button=Button(vent,text="Borrar area de datos", command= clearTextarea)
save_button.place(relx=0.455,rely=0.7,anchor=CENTER)
exist_button=Button(vent,text="Añadir datos al campo de entrada", command= addData)
exist_button.place(relx=0.7,rely=0.7,anchor=CENTER)


vent.mainloop()