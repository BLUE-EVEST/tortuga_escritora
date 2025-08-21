from re import A
from turtle import pendown


class Tortuga_Recorre:
    def __init__(self):
        self.a = 100
        self.b = 200
        self.Diccionario = [{"letra":"A","Funcion":self.Letra_A},
                            {"letra":"B","Funcion":self.Letra_B},
                            {"letra":"C","Funcion":self.Letra_C},
                            {"letra":"D","Funcion":self.Letra_D},
                            {"letra":"E","Funcion":self.Letra_E},
                            {"letra":"F","Funcion":self.Letra_F},
                            {"letra":"G","Funcion":self.Letra_G},
                            {"letra":"H","Funcion":self.Letra_H},
                            {"letra":"I","Funcion":self.Letra_I},
                            {"letra":"J","Funcion":self.Letra_J},
                            {"letra":"K","Funcion":self.Letra_K},
                            {"letra":"L","Funcion":self.Letra_L},
                            {"letra":"O","Funcion":self.Letra_O},
                            {"letra":"P","Funcion":self.Letra_P},
                            {"letra":"Q","Funcion":self.Letra_Q},
                            {"letra":"R","Funcion":self.Letra_R},
                            {"letra":"T","Funcion":self.Letra_T},
                            {"letra":"U","Funcion":self.Letra_U},
                            {"letra":"V","Funcion":self.Letra_V},
                            {"letra":"X","Funcion":self.Letra_X}] #{"letra":"","Funcion":self.Letra_}

    def Letra_A(self):
        #Letra A
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.goto(self.a/2,self.b)
        t.pendown()
        t.goto(self.a,0)

        t.penup()
        t.goto(4*self.a/5,self.b/3)
        t.pendown()
        t.goto(self.a/5,self.b/3)

    def Letra_B(self):
        #Letra B
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.pendown()
        t.goto(0,self.b)

        t.goto(self.a/4,self.b)
        t.circle(-self.a/2,180)
        print(t.position())
        t.goto(0,self.b/2)
        # t.penup()
        t.goto(2*self.a/3,self.b/2)
        t.pendown()

        t.right(180)
        t.circle(-self.a/2,180)
        t.goto(0,0)

        t.penup()
        t.goto(self.a,0)


    def Letra_C(self):
        #Letra C
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.penup()
        t.goto(self.a,3*self.b/4)
        t.pendown()
        #print(t.position())
        t.left(90)
        t.circle(50,180)
        #print(t.position())

        t.goto(0,self.b/4)
        t.pendown()
        t.circle(50,180)

    def Letra_D(self):
        #letra D
        import turtle

        t = turtle.Turtle()

        t.speed(1)
        t.pendown()
        t.goto(0,self.b)
        t.circle(-self.a,180)

    def Letra_E(self):
        #letra E
        import turtle

        t = turtle.Turtle()

        t.speed(1)
        t.pendown()
        t.goto(0,self.b)
        t.goto(self.a,self.b)

        t.penup()
        t.goto(0,self.b/2)
        t.pendown()
        t.goto(2*self.a/3,self.b/2)
        t.penup()
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.goto(self.a,0)

    def Letra_F(self):
        #letra f
        import turtle

        t = turtle.Turtle()

        t.speed(1)
        t.pendown()
        t.goto(0,self.b)
        t.goto(self.a,self.b)

        t.penup()
        t.goto(0,self.b/2)
        t.pendown()
        t.goto(2*self.a/3,self.b/2)

    def Letra_G(self):
        #Letra G

        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.penup()
        t.goto(self.a,3*self.b/4)
        t.pendown()
        #print(t.position())
        t.left(90)
        t.circle(50,180)
        #print(t.position())

        t.goto(0,self.b/4)
        t.pendown()
        t.circle(50,180)
        print(t.position())
        t.goto(self.a,self.b/2)
        t.goto(self.a/2,self.b/2)
        t.goto(self.a/2,self.b/3)

    def Letra_H(self):
        #letra H
        import turtle

        t = turtle.Turtle()

        t.speed(1)
        t.pendown()
        t.goto(0,self.b)
        t.goto(0,self.b/2)
        t.goto(self.a,self.b/2)
        t.goto(self.a,self.b)
        t.goto(self.a,0)


    def Letra_I(self):
        #letra I
        import turtle

        t = turtle.Turtle()

        t.speed(1)
        t.penup()
        t.goto(0,0)
        print(t.position())
        t.goto(self.a/2,0)
        t.pendown()
        print(t.position())

        t.left(90)
        t.forward(self.b)
        print(t.position())

        t.penup()
        t.goto(0,self.b)
        t.pendown()
        print(t.position())

        t.right(90)
        t.forward(self.a)
        print(t.position())

        t.penup()
        t.goto(0,0)
        t.pendown()

        t.forward(self.a)

    def Letra_J(self):
        #Letra J
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.penup()
        t.goto(0,self.b)
        t.pendown()
        t.goto(self.a,self.b)
        t.goto(self.a/2,self.b)
        t.goto(self.a/2,self.b/8)
        print(t.position())
        t.right(90)
        t.circle(-self.a/4,180)
        print(t.position())

    def Letra_K(self):
        #letra K
        import turtle

        t = turtle.Turtle()

        t.speed(1)
        t.pendown()
        t.goto(0,self.b)
        t.goto(0,self.b/2)
        t.goto(self.a,self.b)
        t.goto(0,self.b/2)
        t.goto(self.a,0)

    def Letra_L(self):
        #letra L
        import turtle

        t = turtle.Turtle()

        t.speed(1)
        t.penup
        t.goto(self.a,0)
        t.goto(0,0)
        t.pendown()          
        t.goto(0,self.b)
      

    def Letra_O(self):
        #Letra O
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.penup()
        t.goto(self.a,3*self.b/4)
        t.pendown()
        #print(t.position())
        t.left(90)
        t.circle(50,180)
        #print(t.position())

        t.goto(0,self.b/4)
        t.pendown()
        t.circle(50,180)

        t.goto(self.a,3*self.b/4)
        t.pendown()

    def Letra_P(self):
        #Letra P
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.pendown()
        t.goto(0,self.b)
        t.goto(self.a/2,self.b)

        t.circle(-self.a/2,180)
        t.goto(0,self.b/2)
        print(t.position())

    def Letra_Q(self):
        #Letra Q
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.penup()
        t.goto(self.a,3*self.b/4)
        t.pendown()
        #print(t.position())
        t.left(90)
        t.circle(50,180)
        #print(t.position())

        t.goto(0,self.b/4)
        t.pendown()
        t.circle(50,180)

        t.goto(self.a,3*self.b/4)
        t.pendown()

        t.penup()
        t.goto(self.a/2,self.b/2)

        t.pendown()
        t.goto(self.a,0)

    def Letra_R(self):
        #Letra R
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.pendown()
        t.goto(0,self.b)
        t.goto(self.a/2,self.b)

        t.circle(-self.a/2,180)
        print(t.position())
        t.goto(0,self.b/2)
        t.goto(self.a/2,self.b/2)
        t.goto(self.a,0)
        # print(t.position())

    def Letra_T(self):
        #Letra T
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.penup()
        t.goto(0,self.b)
        t.pendown()
        t.goto(self.a,self.b)
        t.goto(self.a/2,self.b)
        t.goto(self.a/2,0)

    def Letra_U(self):
        import turtle

        t = turtle.Turtle()
        # LETRA "U"

        t.speed(1)
        t.penup()
        t.goto(0,self.b)
        #print(t.position())

        t.pendown()
        t.goto(0, self.b/2)
        #print(tortugui.position())

        t.right(90)
        t.circle(self.a/2,180)
        #print(tortugui.position())

        t.pendown()
        t.goto(self.a,self.b)
        #print(tortugui.position())

    def Letra_V(self):
        #Letra V
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.penup()
        t.goto(0,self.b)
        t.pendown()
        t.goto(self.a/2,0)
        t.goto(self.a,self.b)

    def Letra_X(self):
        #Letra X
        import turtle
        t = turtle.Turtle()
        t.speed(1)

        t.goto(self.a,self.b)
        t.penup()
        t.goto(0,self.b)
        t.pendown()
        t.goto(self.a,0)
            




    def Escribir(self, nombre):
        for letra in nombre.upper():
            for recorrer in self.Diccionario:
                if recorrer["letra"] == letra:
                    recorrer["Funcion"]()

torituga = Tortuga_Recorre()
nombre = input("INGRESA TU NOMBRE: ")
torituga.Escribir(nombre)
#torituga.Letra_Q()
