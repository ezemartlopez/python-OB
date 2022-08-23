"""En este segundo ejercicio, tendréis que crear una interfaz sencilla 
la cual debe de contener una lista de elementos seleccionables, 
también debe de tener un label con el texto que queráis."""
from tkinter import Tk,StringVar
from tkinter import ttk

Centro = 'center'

#Ventana principal
root = Tk()
#Labels
label_main = ttk.Label(root,text="Lista de Sistemas Operativos mas conocidos")
label_main.pack(anchor=Centro)
#Radiobuttons
seleccionado = StringVar()

rb_1 = ttk.Radiobutton(root,text='GNU/Linux',value='op1',variable=seleccionado)
rb_2 = ttk.Radiobutton(root,text='Mac OS',value='op2',variable=seleccionado)
rb_3 = ttk.Radiobutton(root,text='Windows',value='op3',variable=seleccionado)
rb_4 = ttk.Radiobutton(root,text='Ubuntu',value='op4',variable=seleccionado)
#Posicionamiento Radio Buttons
rb_1.pack(anchor=Centro)
rb_2.pack(anchor=Centro)
rb_3.pack(anchor=Centro)
rb_4.pack(anchor=Centro)


if __name__=='__main__':
    root.mainloop()
