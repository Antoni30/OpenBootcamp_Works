from ssl import AlertDescription
import tkinter
from tkinter import ttk
from tkinter import messagebox

def enviar(event):
    seleccionado.set(value="0")
#Ventanas
window=tkinter.Tk()
label= tkinter.Label(window,text="Quieres comprar algo?")
label.pack()
#Radio botones
seleccionado= tkinter.StringVar(value=0)
r1=tkinter.Radiobutton(window,text="Si",value="Si",variable=seleccionado)
r1.pack()
r2=tkinter.Radiobutton(window,text="No",value="No",variable=seleccionado)
r2.pack()
r3=tkinter.Radiobutton(window,text="Quizas",value="Quizas",variable=seleccionado)
r3.pack()
#Boton de eventos
button_selec=tkinter.Button(window,text='Reiniciar')
button_selec.pack()
button_selec.bind('<Button-1>',enviar)
window.mainloop()