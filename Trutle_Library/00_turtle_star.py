import turtle

window = turtle.Screen()    # Generamos una ventana
tortuga = turtle.Turtle()

for i in range(5):
    tortuga.forward(100)    # Forward indica que vaya hacia adelante
    tortuga.right(144)      #Rigth gira a la derecha 144 grados.   

window.mainloop()           # Método para evitar cerrar ventana 

