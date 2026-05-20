from tkinter import *
from tkinter import messagebox


vent= Tk()
vent.geometry("400x400")
vent.title("Reporte_fiebre :P")

question1_radioButton=StringVar(value="0")

Question1=Label(vent, text="¿Tienes dolor de cabeza o dolor de garganta?")
Question1.pack()
question1_r1=Radiobutton(vent,text = "si", variable=question1_radioButton, value= "si")
question1_r1.pack()
question1_r2=Radiobutton(vent,text = "no", variable=question1_radioButton, value= "no")
question1_r2.pack()

question2_radioButton=StringVar(value="0")

Question2= Label(vent, text="¿Tienes temperatura corporal alta?")
Question2.pack()
question2_r1=Radiobutton(vent,text = "si", variable=question2_radioButton, value= "si")
question2_r1.pack()
question2_r2=Radiobutton(vent,text = "no", variable=question2_radioButton, value= "no")
question2_r2.pack()


question3_radioButton=StringVar(value="0")

Question3= Label(vent, text="¿Tienes algun enrojecimiento de ojos?")
Question3.pack()
question3_r1=Radiobutton(vent,text = "si", variable=question3_radioButton, value= "si")
question3_r1.pack()
question3_r2=Radiobutton(vent,text = "no", variable=question3_radioButton, value= "no")
question3_r2.pack()


def fever_score():
    score = 0
    if question1_radioButton.get()=="si":
        print(question1_radioButton)
        score = score+20
        print(score)
    if question2_radioButton.get()=="si":
        print(question2_radioButton)
        score = score+20
        print(score)
    if question3_radioButton.get()=="si":
        print(question3_radioButton)
        score = score+20
        print(score)
    if score <=20:
        messagebox.showinfo("Reporte", "No es necesario que veas un medico.")
    elif score > 20 and  score <=40:
        messagebox.showwarning("Reporte", " Es posible que necesites ver a un medico")
    else :
        messagebox.showerror("Reporte","Se recomienda ir a ver un medico")
        

    
btn = Button(vent,text= "Haz click aqui",command=fever_score)
btn.pack()

vent.mainloop()