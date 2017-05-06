

#var1=20
#var2=0
#while var1>var2:
#    var2=var2+1
#    print "AHH"



#longitud =10

#for i in range (0,longitud):
      #  print "*"*i  #una multiplicacion es repetir



#def suma(a, b):
#    return a+b

#print suma(4,5)


#Clases

class jugador:
    def __init__(self,xo):
        self.x=xo
        #self.vida=25

    def dibujar(self):
        print" "*self.x+"*"
    def mover(self,dx):
        self.x=self.x+dx

personaje=jugador(3)

#Para llamar un metodo de clase debo poner un punto
personaje.dibujar()
