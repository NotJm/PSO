import numpy as np
from enum import Enum
from abc import ABC, abstractmethod

class TipoProblema(Enum):
    CONSTRAINED = 1
    UNCONSTRAINED = 2


class Problema(ABC):
    
    def __init__(self, tipo: TipoProblema):
        self.tipo = tipo
        
    @abstractmethod
    def fitness(self,x):
        pass



#Problema 01
class CEC2006_G01:
    
    

    
    @staticmethod
    def cec2006_g01_aptitud(individuo:np.array):     
        sum1 = np.sum(individuo[0:4])
        sum2 = np.sum(individuo[0:4]**2)
        sum3 = np.sum(individuo[4:13])
        f_x = 5 * sum1 - 5 * sum2 - sum3
        return f_x

    @staticmethod
    def cec2006_g01_g1(x):
        return 2 * x[0] + 2 * x[1] + x[9] + x[10] - 10  # restriccion 1 de desigualdad <= 0
    
    @staticmethod
    def cec2006_g01_g2(x):
        return 2 * x[0] + 2 * x[2] + x[9] + x[11] - 10  # restriccion 2 de desigualdad <= 0
    
    @staticmethod
    def cec2006_g01_g3(x):
        return 2 * x[1] + 2 * x[2] + x[10] + x[11] - 10 # restriccion 3 de desigualdad <= 0
    
    @staticmethod
    def cec2006_g01_g4(x):
        return -8 * x[0] + x[9] # restriccion 4 de desigualdad <= 0
    
    @staticmethod
    def cec2006_g01_g5(x):
        return -8 * x[1] + x[10] # restriccion 5 de desigualdad <= 0
    
    @staticmethod
    def cec2006_g01_g6(x):
        return -8 * x[2] + x[11] # restriccion 6 de desigualdad <= 0
    
    @staticmethod              
    def cec2006_g01_g7(x):
        return -2 * x[3] - x[4] + x[9] #restriccion 7 de desigualdad <= 0

    @staticmethod
    def cec2006_g01_g8(x):
        return -2 * x[5] - x[6] + x[10] # restriccion 8 de desigualdad <= 0

    @staticmethod
    def cec2006_g01_g9(x):
        return -2 * x[7] - x[8] + x[11] # restriccion 9 de desigualdad <= 0
    


#Notas: x es un arrelo de tamaño t= 13 y 0 ≤ xi ≤ 1(i = 1,...,9),0 ≤ xi ≤ 100(i = 10,11,12) 

    
#********************************************************************************************************************************

#Problema 02

class CEC2006_g02:

    @staticmethod
    def CEC2006_g02_aptitud(individuo: np.array):
        sum_cos4 = np.sum(np.cos(individuo)**4)
        prod_cos2 = np.prod(np.cos(individuo)**2)
        sum_ix2 = np.sum((np.arange(1, len(individuo) + 1) * individuo**2))
        f_x = -abs((sum_cos4 - 2 * prod_cos2) / np.sqrt(sum_ix2))
        return f_x

    @staticmethod
    def CEC2006_g02_g1(x):  # restriccion 1 de desigualdad <= 0
        product_x = np.prod(x)
        result = 0.75 - product_x
        return result

    @staticmethod
    def CEC2006_g02_g2(x):  # restriccion 2 de desigualdad <= 0
        sum_x = np.sum(x)
        n = len(x)
        result = sum_x - 7.5 * n
        return result


#Notas: X es un arreglo de tamaño  t=20, 0<Xi<=10, (i=1,2,...,t)

#********************************************************************************************************************************

#Problema 03

class CEC2006_G03:
    
    @staticmethod
    def cec2006_g03_aptitud(individuo:np.array):     
        n = len(individuo)
        product_x = np.prod(individuo)
        f_x = -(np.sqrt(n)**n * product_x)
        return f_x

    @staticmethod
    def cec2006_g03_h1(x): # restriccion 1 de igualdad = 0
        sum_x_squared = np.sum(x**2) 
        return sum_x_squared - 1

#Notas: donde x es de tamaño t=10, 0 ≤ xi ≤ 1(i = 1,...,n).

#********************************************************************************************************************************

#Problema 04

class CEC2006_G04:

    @staticmethod
    def cec2006_g04_aptitud(individuo:np.array):
        x1, x3, x5 = individuo[0], individuo[2], individuo[4]
        f_x = 5.3578547 * x3**2 + 0.8356891 * x1 * x5 + 37.293239 * x1 - 40792.141
        return f_x
    
    def cec2006_g04_g1(x): # restriccion 1 de desigualdad <= 0
        return 85.334407 + 0.0056858 * x[1] * x[4] + 0.0006262 * x[0] * x[3] - 0.0022053 * x[2] * x[4] - 92

    @staticmethod
    def cec2006_g04_g2(x): # restriccion 2 de desigualdad <= 0
        return -85.334407 - 0.0056858 * x[1] * x[4] - 0.0006262 * x[0] * x[3] + 0.0022053 * x[2] * x[4]

    @staticmethod
    def cec2006_g04_g3(x): # restriccion 3 de desigualdad <= 0
        return 80.51249 + 0.0071317 * x[1] * x[4] + 0.0029955 * x[0] * x[1] + 0.0021813 * x[2]**2 - 110

    @staticmethod
    def cec2006_g04_g4(x): # restriccion 4 de desigualdad <= 0
        return -80.51249 - 0.0071317 * x[1] * x[4] - 0.0029955 * x[0] * x[1] - 0.0021813 * x[2]**2 + 90

    @staticmethod
    def cec2006_g04_g5(x): # restriccion 5 de desigualdad <= 0
        return 9.300961 + 0.0047026 * x[2] * x[4] + 0.0012547 * x[0] * x[2] + 0.0019085 * x[2] * x[3] - 25

    @staticmethod
    def cec2006_g04_g6(x): # restriccion 6 de desigualdad <= 0
        return -9.300961 - 0.0047026 * x[2] * x[4] - 0.0012547 * x[0] * x[2] - 0.0019085 * x[2] * x[3] + 20


#Notas: donde 78 ≤ x1 ≤ 102,33 ≤ x2 ≤ 45 y 27 ≤ xi ≤ 45(i = 3,4,5)

#********************************************************************************************************************************

#Problema 05

class CEC2006_G05:

    @staticmethod
    def cec2006_g05_aptitud(individuo:np.array): 
        x1, x2 = individuo[0], individuo[1]
        f_x = 3 * x1 + 0.000001* x1**3 + 2* x2 + (0.000002/3) * x2**3
        return f_x

    @staticmethod
    def cec2006_g05_g1(x): # restriccion 1 de desigualdad <= 0
        return -x[3] + x[2] - 0.55
    
    @staticmethod
    def cec2006_g05_g2(x): # restriccion 2 de desigualdad <= 0
        return -x[2] + x[3] - 0.55
    
    @staticmethod
    def cec2006_g05_h3(x): # restriccion 3 de igualdad = 0
        return 1000 * np.sin(-x[2] - 0.25) + 1000 * np.sin(-x[3] - 0.25) + 894.8 - x[0]
    
    @staticmethod
    def cec2006_g05_h4(x): # restriccion 4 de igualdad = 0
        return 1000 * np.sin(x[2] - 0.25) + 1000 * np.sin(x[2] - x[3] - 0.25) + 894.8 - x[1]
    
    @staticmethod
    def cec2006_g05_h5(x): # restriccion 5 de igualdad = 0
        return 1000 * np.sin(x[3] - 0.25) + 1000 * np.sin(x[3] - x[2] - 0.25) + 1294.8


#Notas: donde 0 ≤ x1 ≤ 1200, 0 ≤ x2 ≤ 1200, −0.55 ≤ x3 ≤ 0.55 y −0.55 ≤ x4 ≤ 0.55.


#********************************************************************************************************************************

#Problema 06
class CEC2006_G06:

    @staticmethod
    def cec2006_g06_aptitud(individuo:np.array): 
        x1, x2 = individuo[0], individuo[1]
        f_x = (x1 -10)**3 + (x2-20)**3
        return f_x
    
    @staticmethod
    def cec2006_g06_g1(x): # restriccion 1 de desigualdad <= 0
        return -(x[0] -5)**2 - (x[1] - 5)**2 +100 
    
    @staticmethod
    def cec2006_g06_g2(x): # restriccion 2 de desigualdad <= 0
        return (x[0] - 6)**2 + (x[1] - 5)**2 - 82.81

#Notas: donde 13 ≤ x1 ≤ 100 y 0 ≤ x2 ≤ 100


#********************************************************************************************************************************

#Problema 07

class CEC2006_G07:

    @staticmethod
    def cec2006_g07_aptitud(individuo:np.array): 
        f_x = (individuo[0]**2 + individuo[1]**2 + individuo[0]*individuo[0] - 14*individuo - 16*individuo[1] + (individuo[2] - 10)**2 + 
                4*(individuo[3] - 5)**2 + (individuo[4] - 3)**2 + 2*(individuo[5] - 1)**2 + 5*individuo[6]**2 + 
                7*(individuo[7] - 11)**2 + 2*(individuo[8] - 10)**2 + (individuo[9] - 7)**2 + 45)
        return f_x

    @staticmethod
    def cec2006_g07_g1(x): # restriccion 1 de desigualdad <= 0
        return -105 + 4 * x[0] + 5 * x[1] - 3 * x[6] + 9 * x[7]
    
    @staticmethod
    def cec2006_g07_g2(x): # restriccion 2 de desigualdad <= 0
        return 10 * x[0] - 8 * x[1] - 17 * x[6] + 2 * x[7]
    
    @staticmethod
    def cec2006_g07_g3(x): # restriccion 3 de desigualdad <= 0
        return -8 * x[0] + 2 * x[1] + 5 * x[8] - 2 * x[9] - 12
    
    @staticmethod
    def cec2006_g07_g4(x): # restriccion 4 de desigualdad <= 0
        return 3 * (x[0] - 2)**2 + 4 * (x[1] - 3)**2 + 2 * x[2]**2 - 7 * x[3] - 120

    @staticmethod
    def cec2006_g07_g5(x): # restriccion 5 de desigualdad <= 0
        return 5 * x[0]**2 + 8 * x[1] + (x[2] - 6)**2 - 2 * x[3] - 40

    @staticmethod
    def cec2006_g07_g6(x): # restriccion 6 de desigualdad <= 0
        return x[0]**2 + 2 * (x[1] - 2)**2 - 2 * x[0] * x[1] + 14 * x[4] - 6 * x[5]

    @staticmethod
    def cec2006_g07_g7(x): # restriccion 7 de desigualdad <= 0
        return 0.5 * (x[0] - 8)**2 + 2 * (x[1] - 4)**2 + 3 * x[4]**2 - x[5] - 30

    @staticmethod
    def cec2006_g07_g8(x): # restriccion 8 de desigualdad <= 0
        return -3 * x[0] + 6 * x[1] + 12 * (x[8] - 8)**2 - 7 * x[9]

    
    #Notas: donde −10 ≤ xi ≤ 10(i = 1,...,10)
    
#********************************************************************************************************************************

#Problema 08

class CEC2006_G08:
    
    @staticmethod
    def cec2006_g08_aptitud(individuo:np.array): 
        num = (np.sin(2 * np.pi * individuo[0]) ** 3) * np.sin(2 * np.pi * individuo[1])
        den = individuo[0]**3 * (individuo[0] + individuo[1])
        return - (num / den)
    
    @staticmethod
    def cec2006_g08_g1(x): # restriccion 1 de desigualdad <= 0
        return x[0] ** 2 - x[1] + 1 
    
    @staticmethod
    def cec2006_g08_g2(x): # restriccion 2 de desigualdad <= 0
        return 1 - x[0] + (x[1] - 4) ** 2

    #245, 278
    
    
#********************************************************************************************************************************

#Problema 9

class CEC2006_G09:
    
    @staticmethod
    def cec2006_g09_aptitud(individuo:np.array): 
        f_x = ((individuo[0] - 10)**2 + 5 * (individuo[1] - 12)**2 + individuo[2]**4 + 3 * (individuo[3] - 11)**2
           + 10 * individuo[4]**6 + 7 * individuo[5]**2 + individuo[6]**4 - 4 * individuo[5] * individuo[6]
           - 10 * individuo[5] - 8 * individuo[6])
        return f_x
    
    @staticmethod
    def cec2006_g09_g1(x): # restriccion 1 de desigualdad <= 0
        return -127 + 2 * x[0]**2 + 3 * x[1]**4 + x[2] + 4 * x[3]**2 + 5 * x[4]
    
    @staticmethod
    def cec2006_g09_g2(x): # restriccion 2 de desigualdad <= 0
        return -282 + 7 * x[0] + 3 * x[1] + 10 * x[2]**2 + x[3] - x[4]
    
    @staticmethod
    def cec2006_g09_g3(x): # restriccion 3 de desigualdad <= 0
        return -196 + 23 * x[0] + x[1]**2 + 6 * x[5]**2 - 8 * x[6]
    
    @staticmethod
    def cec2006_g09_g4(x): # restriccion 4 de desigualdad <= 0
        return 4 * x[1]**2 + x[2]**2 - 3 * x[0] * x[1] + 2 * x[3]**2 + 5 * x[5] - 11 * x[6]    


#********************************************************************************************************************************

#Problema 10


#********************************************************************************************************************************

#Problema 11


#********************************************************************************************************************************

#Problema 12


#********************************************************************************************************************************

#Problema 13


#********************************************************************************************************************************

#Problema 14


#********************************************************************************************************************************

#Problema 15



#********************************************************************************************************************************

#Problema 16



#********************************************************************************************************************************

#Problema 17