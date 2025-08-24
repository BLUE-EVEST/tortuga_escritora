#Recordatorio: llama siempre la libreria antes de las acciones pa eviar el error que cometi antes
# la cual fue llamar la libreria turtle en cada letra :c
import turtle

class Tortuga_Recorre:
    def __init__(self):
        self.alto_total = 200
        self.separacion = 50 # la separacion de cada letra "A" 50 pixeles mas alla "B" / 50 pixeles es muy grande
        self.margen = 50  
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
                            {"letra":"M","Funcion":self.Letra_M},
                            {"letra":"N","Funcion":self.Letra_N},
                            {"letra":"Ñ","Funcion":self.Letra_ANTIGRINGOS},
                            {"letra":"O","Funcion":self.Letra_O},
                            {"letra":"P","Funcion":self.Letra_P},
                            {"letra":"Q","Funcion":self.Letra_Q},
                            {"letra":"R","Funcion":self.Letra_R},
                            {"letra":"S","Funcion":self.Letra_S},
                            {"letra":"T","Funcion":self.Letra_T},
                            {"letra":"U","Funcion":self.Letra_U},
                            {"letra":"V","Funcion":self.Letra_V},
                            {"letra":"W","Funcion":self.Letra_W},
                            {"letra":"X","Funcion":self.Letra_X},
                            {"letra":"Y","Funcion":self.Letra_Y},
                            {"letra":"Z","Funcion":self.Letra_Z}] #{"letra":"","Funcion":self.Letra_}

    def configuracion_pantalla(self, total_letras):
        ancho_total = (total_letras * self.separacion) + (2 * self.margen)
        self.pantalla = turtle.Screen()
        self.pantalla.setup(ancho_total, self.alto_total)
        return ancho_total
# NO TOCAR TOTAL_LETRAS EN COFIGURACION DE LA POSCICION DE LETRAS / NI YO SE PQ FUNCIONA SI ESTA PUESTO
# SI FUNCIONA NO LO TOQUES XD
    def configurar_pos_letra(self, indice,total_letras, ancho_total):
        x = -ancho_total/2 + self.margen + (indice * self.separacion) + (self.separacion / 2)
        y = -self.alto_total/2 + 100
        return x, y


    def Letra_A(self, x, y):
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x, y)
        print(t.position())
        t.pendown()

        t.goto(x + 20, y + 80)
        print(t.position())
        t.goto(x + 40, y)
        print(t.position())

        t.penup()
        t.goto(x + 10, y + 40)
        t.pendown()
        t.goto(x + 30, y + 40)
        print(t.position())

    def Letra_B(self, x, y):
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x, y)
        t.pendown()

        t.goto(x, y + 80)
        t.goto(x + 20, y + 80)
        t.circle(-20, 180)

        t.goto(x, y + 40)
        print(t.position())
        t.goto(x + 20, y + 40)
        print(t.position())
        t.right(180)
        t.circle(-20, 180)
        t.goto(x, y)
        t.hideturtle()

    def Letra_C(self, x, y):
        #Letra C
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x + 40, y + 60)
        print(x)
        print(t.position())
        t.pendown()
        t.left(90)
        print(t.position())
        t.circle(20,180)
        print(t.position())
        t.goto(x,y +20)
        print(t.position())
        t.circle(20,180)


    def Letra_D(self,x,y):
        #letra D
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x,y+80)
        t.circle(-40,180)

    def Letra_E(self,x,y):
        #letra E
        t = turtle.Turtle()
        t.speed(1)
        t.pensize(4)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x,y+80)
        t.goto(x+40,y+80)
        t.goto(x,y+80)
        t.goto(x,y+40)
        t.goto(x+20,y+40)
        t.goto(x,y+40)
        t.goto(x,y)
        t.goto(x+40,y)



    def Letra_F(self,x,y):
        #letra f
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x,y+80)
        t.goto(x+40,y+80)
        t.goto(x,y+80)
        t.goto(x,y+40)
        t.goto(x+20,y+40)

    def Letra_G(self,x,y):
        #Letra G
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x + 40, y + 60)
        print(x)
        print(t.position())
        t.pendown()
        t.left(90)
        print(t.position())
        t.circle(20,180)
        t.goto(x,y +20)
        print(t.position())
        t.circle(20,180)
        t.goto(x+40,y+40)
        t.goto(x+20,y+40)
        t.goto(x+20,y+30)

    def Letra_H(self,x,y):
        #letra H
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x,y+80)
        t.goto(x,y+40)
        t.goto(x+40,y+40)
        t.goto(x+40,y+80)
        t.goto(x+40,y)


    def Letra_I(self,x,y):
        #letra I
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x+40,y)
        t.goto(x+20,y)
        t.goto(x+20,y+80)
        t.goto(x,y+80)
        t.goto(x+40,y+80)

    def Letra_J(self,x,y):
        #Letra J
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)

        t.penup()
        t.goto(x,y+80)
        t.pendown()
        t.goto(x+40,y+80)
        t.goto(x+20,y+80)
        t.goto(x+20,y+20)
        t.right(90)
        t.circle(-10,180)


    def Letra_K(self,x,y):
        #letra K
        t = turtle.Turtle()
        t.pensize(4)

        t.speed(1)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x,y+80)
        t.goto(x,y+40)
        t.goto(x+40,y+80)
        t.goto(x,y+40)
        t.goto(x+40,y)


    def Letra_L(self,x,y):
        #letra L
        t = turtle.Turtle()
        t.pensize(4)

        t.speed(1)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x,y+80)
        t.goto(x,y)
        t.goto(x+40,y)

    def Letra_M(self,x,y):
        #letra M
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x,y+80)
        t.goto(x+20,y)
        t.goto(x+40,y+80)
        t.goto(x+40,y)


    def Letra_N(self,x,y):
        #letra N
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x,y+80)
        t.goto(x+40,y)
        t.goto(x+40,y+80)

    def Letra_ANTIGRINGOS(self,x,y):
        #letra Ñ
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x,y+60)
        t.goto(x+40,y)
        t.goto(x+40,y+60)
        t.penup()
        t.goto(x+30,y+65)
        t.pendown()
        t.goto(x+30,y+70)
        t.left(90)
        print(t.position())
        t.circle(5,180)
        t.circle(-5,180)
        print(t.position())
        t.goto(x+10,y+75)

    def Letra_O(self, x , y):
        #Letra O
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x + 40, y + 60)
        print(x)
        print(t.position())
        t.pendown()
        t.left(90)
        print(t.position())
        t.circle(20,180)
        print(t.position())
        t.goto(x,y +20)
        print(t.position())
        t.circle(20,180)
        t.goto(x + 40, y + 60)

    def Letra_P(self, x, y):
        #Letra P
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x, y + 80)
        t.goto(x + 20, y + 80)
        t.circle(-20, 180)
        print(t.position())
        t.goto(x,y+40)


    def Letra_Q(self, x , y):
        #Letra Q
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x + 40, y + 60)
        print(x)
        print(t.position())
        t.pendown()
        t.left(90)
        print(t.position())
        t.circle(20,180)
        print(t.position())
        t.goto(x,y +20)
        print(t.position())
        t.circle(20,180)
        t.goto(x + 40, y + 60)
        t.penup()
        t.goto(x+20,y+50)
        t.pendown()
        t.goto(x+40,y)

    def Letra_R(self,x ,y):
        #Letra R
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x, y + 80)
        t.goto(x + 20, y + 80)
        t.circle(-20, 180)
        print(t.position())
        t.goto(x,y+40)
        t.goto(x+40,y)

    def Letra_S(self,x,y):
        #Letra S
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x + 40, y + 60)
        t.pendown()
        t.left(90)
        t.circle(20,90)
        t.circle(20,180)
        t.circle(-20,180)
        t.circle(-20,90)


    def Letra_T(self,x,y):
        #Letra T
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x+20, y)
        t.pendown()
        t.goto(x+20,y+80)
        t.goto(x+40,y+80)
        t.goto(x,y+80)


    def Letra_U(self,x,y):
        #LETRA "U"
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)
        t.penup()
        t.goto(x,y +80)
        t.pendown()

        t.goto(x,y+20)
        print(t.position())
        t.right(90)
        t.circle(20,180)
        t.goto(x+40,y+80)

    def Letra_W(self,x,y):
        #Letra W
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)

        t.penup()
        t.goto(x,y+80)
        t.pendown()
        t.goto(x+10,y)
        t.goto(x+20,y+40)
        t.goto(x+30,y)
        t.goto(x+40,y+80)

    def Letra_V(self,x,y):
        #Letra V
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)

        t.penup()
        t.goto(x,y+80)
        t.pendown()
        t.goto(x+20,y)
        t.goto(x+40,y+80)

    def Letra_X(self,x,y):
        #Letra X
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)

        t.penup()
        t.goto(x,y+80)
        t.pendown()
        t.goto(x+40,y)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x+40,y+80)


    def Letra_Y(self,x,y):
        #Letra Y
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)

        t.penup()
        t.goto(x,y+80)
        t.pendown()
        t.goto(x+20,y+50)
        t.goto(x+40,y+80)
        t.goto(x+20,y+50)
        t.goto(x+20,y)


    def Letra_Z(self,x,y):
        #Letra Z
        t = turtle.Turtle()
        t.pensize(4)
        t.speed(1)

        t.penup()
        t.goto(x,y+80)
        t.pendown()
        t.goto(x+40,y+80)
        t.goto(x,y)
        t.goto(x+40,y)


    def Escribir(self, nombre):
        total_letras = len(nombre)
        ancho_total = self.configuracion_pantalla(total_letras)
        for indice, letra in enumerate(nombre.upper()):
            x, y = self.configurar_pos_letra(indice, total_letras, ancho_total)
            for recorrer in self.Diccionario:
                if recorrer["letra"] == letra:
                    recorrer["Funcion"](x, y)
                    break

torituga = Tortuga_Recorre()
nombre = input("INGRESA TU NOMBRE: ")
torituga.Escribir(nombre)

