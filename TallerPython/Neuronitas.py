#factor de aprendizaje = gamma(umbral - y)x
import_random

class neurona:
    def __init__(self,factordeaprendizaje):
        self.factaprendizaje= factordeaprendizaje
        self.w=[]
        self.umbral=random.random()
        for i in range(0,2):
            self.w.append(random.random()) #Con esto se crea una lista de pesos

    def salida (self,vectordeentrada)
        sumatotal=0
        for i in range (0,2):
            sumatotal=sumatotal + vectordeentrada[i]*self.w[i]
        return sumatotal + sef.umbral
'''
    def funcionescalon(self,vectentrada)

        if vectentrada <1:
            x=self.salida(vectentrada)

        else:
            return -1
'''
#el objetivo es que aprenda, que al final se tenga una funccion OR
    
    def entrenar(self,entradas):
        for i in range (len(entradas)):
            saldeseada = entradas[i][-1]
            x1=entradas[i][0]
            x2=entradas[i][2]

            error = saldeseada - self.salida ([x1,x2])**2
            dw1=self.factaprendizaje *error *x1
            dw2=self.factaprendizaje *error *x2
            dumbral=self.factaprendizaje * error

            self.w[0]= self.w[0]+dw1
            self.w[1]=self.w[1]+dw2
            self.w[2]= self.umbral+dumbral
    

adeline = neurona(0.2)
print adeline.funcionescalon([-1,-1])

for i in range(0,100):
adeline.entrenar([-1,-1,-1])

#[[-1,-1,-1],[-1,1,1]]
