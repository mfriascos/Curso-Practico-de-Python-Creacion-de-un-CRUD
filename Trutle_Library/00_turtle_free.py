import turtle

window = turtle.Screen()    # Generamos una ventana
tortuga = turtle.Turtle()


for i in range(18):
    tortuga.left(111.8)
    tortuga.forward(120)        # Forward indica que vaya hacia adelante 
    tortuga.right(63.62)
    tortuga.forward(60)
    tortuga.right(89.98)
    tortuga.forward(60)
    tortuga.right(68.18)
    tortuga.forward(120)

window.mainloop()           # Método para evitar cerrar ventana 

