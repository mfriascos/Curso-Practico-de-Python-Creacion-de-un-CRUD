import turtle

window = turtle.Screen()    # Generamos una ventana
tortuga = turtle.Turtle()

for i in range(4):
    tortuga.forward(100)        # Forward indica que vaya hacia adelante 
    tortuga.right(90)

window.mainloop()           # Método para evitar cerrar ventana 

