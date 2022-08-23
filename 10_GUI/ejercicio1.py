"""En este ejercicio tenéis que crear una lista de RadioButton que muestre 
la opción que se ha seleccionado 
y que contenga un botón de reinicio para que deje todo como al principio.
Al principio no tiene que haber una opción seleccionada.
"""
from tkinter import Tk,StringVar
from tkinter import ttk

def reiniciarCeldas():
    seleccionado.set(None)

#Ventana principal
root = Tk()

#Radiobuttons
seleccionado = StringVar()

rb_1 = ttk.Radiobutton(root,text='Opcion 1',value='op1',variable=seleccionado)
rb_2 = ttk.Radiobutton(root,text='Opcion 2',value='op2',variable=seleccionado)
rb_3 = ttk.Radiobutton(root,text='Opcion 3',value='op3',variable=seleccionado)
#Buttons
b_reinicio = ttk.Button(root,text='Reiniciar',command=reiniciarCeldas)
#Posicionamiento
rb_1.grid(column=0,row=1,pady=5,padx=10)
rb_2.grid(column=0,row=2,pady=5,padx=10)
rb_3.grid(column=0,row=3,pady=5,padx=10)
b_reinicio.grid(column=0,row=4,pady=5,padx=10)

if __name__=='__main__':
    root.mainloop()
