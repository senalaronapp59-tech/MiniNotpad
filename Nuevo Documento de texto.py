from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import os

vent= Tk()
vent.minsize(650,650)
vent.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))

label_file_name = Label(vent, text= "nombre del archivo")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(vent)
input_file_name.place(relx=0.46,rely=0.03,anchor= CENTER)

my_text= Text(vent,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

name = ""
def openFile():
    global name
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    
    text_file = filedialog.askopenfilename(title= "abrir el archivo de texto",
                                           filetypes=(("Archivos de texto", ".txt"),))
    
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    vent.title(formated_name)
    text_file = open(name,'r')
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
    
    
def save():
    input_name = input_file_name.get()
    file = open(input_name+".txt", "w")
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("Actualizar", "Exito")
    
def closeWindow():
    vent.destroy()




open_button=Button(vent,image=open_img,text="Abrir el archivo", command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor= CENTER)
save_button=Button(vent, image=save_img,text="Guardar el archivo", command=save)
save_button.place(relx=0.11,rely=0.03,anchor= CENTER)
exit_button=Button(vent,image=exit_img,text="Salir del archivo",command=closeWindow)
exit_button.place(relx=0.17,rely=0.03,anchor= CENTER)



vent.mainloop()