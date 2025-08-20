class Tortuga_Recorre:
    def __init__(self):
        self.a = 100
        self.b = 200
        self.Diccionario = [{"letra":"Q","Funcion":self.Letra_Q}]
    def Letra_Q(self):
        #Letra Q
        import turtle
        t = turtle.Turtle()
        t.speed(2)
        t.penup()
        t.goto(self.a/2,self.b/4)
        t.pendown()
        t.circle(self.a/2)
        t.penup()
        t.goto(self.a/2,self.b/2.5)
        t.pendown()
        t.goto(self.a,self.b/4)

        turtle.exitonclick()
    def Escribir(self, nombre):
        for letra in nombre.upper():
            for recorrer in self.Diccionario:
                if recorrer["letra"] == letra:
                    recorrer["Funcion"]()

torituga = Tortuga_Recorre()
nombre = input("INGRESA TU NOMBRE: ")
torituga.Escribir(nombre)
#torituga.Letra_Q()
