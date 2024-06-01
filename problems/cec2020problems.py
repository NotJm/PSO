import numpy as np
from .Problem import Problem, ProblemType

# Problema 01
class CEC2020_RC01(Problem):
    
    # WITH BOUNDS:
    
    # 0 ≤ x1 ≤ 10, 0 ≤ x2 ≤ 200, 0 ≤ x3 ≤ 100, 0 ≤ x4 ≤ 200,
    # 1000 ≤ x5 ≤ 2000000, 0 ≤ x6 ≤ 600, 100 ≤ x7 ≤ 600, 100 ≤ x8 ≤ 600,
    # 100 ≤ x9 ≤ 900.
    
    SUPERIOR = np.array([10,200,100,200,2000000,600,600,600,900])
    INFERIOR = np.array([0,0,0,0,1000,0,100,100,100])

    def __init__(self):
        rest_h = [
            self.CEC2020_RC01_h1,
            self.CEC2020_RC01_h2,
            self.CEC2020_RC01_h3,
            self.CEC2020_RC01_h4,
            self.CEC2020_RC01_h5,
            self.CEC2020_RC01_h6,
            self.CEC2020_RC01_h7,
            self.CEC2020_RC01_h8,
        ]
        super().__init__(ProblemType.CONSTRAINED, self.SUPERIOR, self.INFERIOR, [],  rest_h)
    
    def fitness(self, individuo: np.array) -> float:
        f_x = 35 * individuo[0]**0.6 + 35 * individuo[1]**0.6
        return f_x

    @staticmethod
    def CEC2020_RC01_h1(x):
        return 200 * x[0] * x[3] - x[2]  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC01_h2(x):
        return 200 * x[1] * x[5] - x[4]  # restriccion 2 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC01_h3(x):
        return x[2] - 10000 * (x[6] - 100)  # restriccion 3 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC01_h4(x):
        return x[4] - 10000 * (300 - x[6])  # restriccion 4 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC01_h5(x):
        return x[2] - 10000 * (600 - x[7]) # restriccion 5 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC01_h6(x):
        return x[4] - 10000 * (900 - x[8]) # restriccion 6 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC01_h7(x):
        if x[7] - 100 <= 0 or 600 - x[6] <= 0:
            return 0
        return x[3] * np.log(x[7] - 100) - x[3] * np.log(600 - x[6]) - x[7] + x[6] + 500

    @staticmethod
    def CEC2020_RC01_h8(x):
        if x[8] - x[6] <= 0 or 600 <= 0:
            return 0 
        return x[5] * np.log(x[8] - x[6]) - x[5] * np.log(600) - x[8] + x[6] + 600

#********************************************************************************************************************************

#Problem 02

class CEC2020_RC02(Problem):
    
    # WITH BOUNDS:
    
    # 10**4 ≤ x1 ≤ 81.9 × 10**4, 10**4 ≤ x2 ≤ 113.1 × 10**4, 10**4 ≤ x3 ≤ 205 × 10**4,
    # 0 ≤ x4, x5, x6 ≤ 5.074 × 10**−2, 100 ≤ x7 ≤ 200, 100 ≤ x8, x9, x10 ≤ 300
    # 100 ≤ x11 ≤ 400.

    
    INFERIOR = np.array([
        10**4,10**4,10**4,0,0,
        0,100,100,100,100,100
    ])
    SUPERIOR = np.array([
        81.9 * 10**4,113.1 * 10**4,205 * 10**4,5.074 * 10**-2,5.074 * 10**-2,
        5.074 * 10**-2,200,300,300,300,400
    ]) 
    
    def __init__(self):
        rest_h = [
            self.CEC2020_RC02_h1, self.CEC2020_RC02_h2, self.CEC2020_RC02_h3,
            self.CEC2020_RC02_h4, self.CEC2020_RC02_h5, self.CEC2020_RC02_h6,
            self.CEC2020_RC02_h7, self.CEC2020_RC02_h8, self.CEC2020_RC02_h9
        ]
        super().__init__(ProblemType.CONSTRAINED, self.SUPERIOR, self.INFERIOR, [],  rest_h)
    
    def fitness(self, individuo: np.array) -> float:
        x = individuo
        f_x = ( x[0] / (120 * x[3]) )**0.6 + ( x[1] / (80 * x[4]) )**0.6 + ( x[2] / (40 * x[5]) )**0.6
        return f_x
    
    @staticmethod
    def CEC2020_RC02_h1(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC02_h2(x):
        return x[1] - 10**4 * (x[7] - x[6])  # restriccion 2 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC02_h3(x):
        return x[2] - 10**4 * (500 - x[7])  # restriccion 3 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC02_h4(x):
        return x[0] - 10**4 * (300 - x[8])  # restriccion 4 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC02_h5(x):
        return x[1] - 10**4 * (400 - x[9])  # restriccion 5 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC02_h6(x):
        return x[3] - 10**4 * (600 - x[10])  # restriccion 6 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC02_h7(x):
        if x[8] - 100 <= 0 or 300 - x[6] <= 0:
            return 0
        return x[3] * np.log(x[8] - 100) - x[3] * np.log(300 - x[6]) - x[8] + x[6] + 400 # restriccion 7 de igualdad = 0
    
    @staticmethod              
    def CEC2020_RC02_h8(x):
        if x[9] - x[6] <= 0 or 400 - x[7] <= 0:
            return 0
        return x[4] * np.log(x[9] - x[6]) - x[4] * np.log(400 - x[7]) - x[9] + x[6] - x[7] + 400 #restriccion 8 de igualdad = 0

    @staticmethod
    def CEC2020_RC02_h9(x):
        if x[10] - x[7] <= 0:
            return 0
        return x[5] * np.log(x[10] - x[7]) - x[5] * np.log(100) - x[10] + x[7] + 100 # restriccion 9 de igualdad = 0

#********************************************************************************************************************************

#Problem 03

class CEC2020_RC03(Problem):
    
    # WITH BOUNDS:
    
    # 0 ≤ x1 ≤ 10, 0 ≤ x2 ≤ 200, 0 ≤ x3 ≤ 100, 0 ≤ x4 ≤ 200,
    # 1000 ≤ x5 ≤ 2000000, 0 ≤ x6 ≤ 600, 100 ≤ x7 ≤ 600, 100 ≤ x8 ≤ 600,
    # 100 ≤ x9 ≤ 900.
    
    SUPERIOR = np.array([100,200,100,100,100,100,200,100,200])
    INFERIOR = np.array([0,0,0,0,0,0,0,0,0])

    def __init__(self):
        rest_h = [
            self.CEC2020_RC03_h1, self.CEC2020_RC03_h2, self.CEC2020_RC03_h3, self.CEC2020_RC03_h4, 
        ]
        rest_g = [
            self.CEC2020_RC03_g1, self.CEC2020_RC03_g2
        ]
        super().__init__(ProblemType.CONSTRAINED, self.SUPERIOR, self.INFERIOR, rest_g,  rest_h)
    
    def fitness(self, individuo: np.array) -> float:
        x = np.copy(individuo)
        f_x = 9 * x[0] + 15 * x[1] - 6 * x[2] - 16 * x[3] - 10(x[4] + x[5])
        return f_x

    @staticmethod
    def CEC2020_RC03_h1(x):
        return x[6] + x[7] - x[3] - x[2]  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC03_h2(x):
        return x[0] - x[4] - x[7]  # restriccion 2 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC03_h3(x):
        return x[1] - x[5] - x[6]  # restriccion 3 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC03_h4(x):
        return x[8] * x[6] + x[8] * x[7] - 3 * x[2] - x[3]   # restriccion 4 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC03_g1(x):
        return x[8] * x[6] + 2 * x[4] - 2.5 * x[0]  # restriccion 5 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC03_g2(x):
        return x[8] * x[7] + 2 * x[5] - 1.5 * x[1] # restriccion 6 de igualdad = 0
    
#********************************************************************************************************************************

#Problem 04

class CEC2020_RC04(Problem):
    
    SUPERIOR = []
    INFERIOR = [] 
    
    def __init__(self):
        rest_h = [
            self.CEC2020_RC04_h1, self.CEC2020_RC04_h2, self.CEC2020_RC04_h3, self.CEC2020_RC04_h4,
            self.CEC2020_RC04_h5, self.CEC2020_RC04_h6, self.CEC2020_RC04_h7, self.CEC2020_RC04_h8,
            self.CEC2020_RC04_h9, self.CEC2020_RC04_h10, self.CEC2020_RC04_h11, self.CEC2020_RC04_h12,
            self.CEC2020_RC04_h13, self.CEC2020_RC04_h14, self.CEC2020_RC04_h15, self.CEC2020_RC04_h16,
            self.CEC2020_RC04_h17, self.CEC2020_RC04_h18, self.CEC2020_RC04_h19, self.CEC2020_RC04_h20,
            self.CEC2020_RC04_h21, self.CEC2020_RC04_h22, self.CEC2020_RC04_h23, self.CEC2020_RC04_h24,
            self.CEC2020_RC04_h25, self.CEC2020_RC04_h26, self.CEC2020_RC04_h27, self.CEC2020_RC04_h28,
            self.CEC2020_RC04_h27, self.CEC2020_RC04_h30, self.CEC2020_RC04_h31, self.CEC2020_RC04_h32,
        ]
        super().__init__(ProblemType.CONSTRAINED, self.SUPERIOR, self.INFERIOR, [],  rest_h)
    
    def fitness(self, individuo: np.array) -> float:
        x = np.copy(individuo)
        f_x = 0.9979 + 0.00432 * x[4] + 0.01517 * x[12]
        return f_x

    @staticmethod
    def CEC2020_RC04_h1(x):
        return x[4] + x[3] + x[2] + x[1] 
    
    @staticmethod
    def CEC2020_RC04_h2(x):
        return x[6] +  x[8] + x[7] # restriccion de igualdad de 0 

    @staticmethod
    def CEC2020_RC04_h3(x):
        return x[9] + x[11] + x[10] + x[12] # restriccion de igualdad de 0 

    @staticmethod
    def CEC2020_RC04_h4(x):
        return x[14] + x[16] + x[17] + x[15] # restriccion de igualdad de 0 

    @staticmethod
    def CEC2020_RC04_h5(x):
        return x[18] + x[20] + x[19] # restriccion de igualdad de 0 

    @staticmethod
    def CEC2020_RC04_h6(x):
        return x[5] * x[21]  -  x[6] * x[22]  -  x[9] * x[23] 

    @staticmethod 
    def CEC2020_RC04_h7(x):
        return  x[5] * x[24]  -  x[6] * x[25]  -  x[9] * x[26] # restricciones de igualdad de 0 

    @staticmethod 
    def CEC2020_RC04_h8(x):
        return x[5] * x[27]  -  x[6] * x[28]  -  x[9] * x[29] # restricciones de igualdad de 0 

    @staticmethod
    def CEC2020_RC04_h9(x):
        return x[13] * x[30]  -  x[14] * x[31]  -  x[18] * x[32] # restricciones de igualdad de 0 

    @staticmethod
    def CEC2020_RC04_h10(x):
        return x[13] * x[33]  -  x[14] * x[34]  -  x[18] * x[35] # restricciones de igualdad de 0 

    @staticmethod
    def CEC2020_RC04_h11(x):
        return x[13] * x[36]  -  x[14] * x[37]  -  x[18] * x[35] # restricciones de igualdad de 0 13

    @staticmethod
    def CEC2020_RC04_h12(x):
        return 0.333[1]   +   x[15] * x[31]  -  x[5] * x[21]    # restricciones de igualdad de 0 

    @staticmethod
    def CEC2020_RC04_h13(x):
        return 0.333[1]   +   x[15] * x[34]  -  x[5] * x[24]    # restricciones de igualdad de 0 

    @staticmethod
    def CEC2020_RC04_h14(x):
        return  0.333[1]   +   x[15] * x[37]  -  x[5] * x[27]    # restricciones de igualdad de 0  

    @staticmethod
    def CEC2020_RC04_h15(x):
        return  0.333[2]   +   x[10] * x[23]  -  x[13] * x[30]    # restricciones de igualdad de 0  

    @staticmethod
    def CEC2020_RC04_h16(x):
        return  0.333[2]   +   x[10] * x[26]  -  x[13] * x[33]    # restricciones de igualdad de 0  

    @staticmethod
    def CEC2020_RC04_h17(x):
        return  0.333[2]   +   x[10] * x[29]  -  x[13] * x[36]    # restricciones de igualdad de 0

    @staticmethod
    def CEC2020_RC04_h18(x):
        return  0.333[3]   +   x[7] * x[22] +   x[11] * x[23]  +   x[16] * x[31] +   x[19] * x[32]     # restricciones de igualdad de 30

    @staticmethod
    def CEC2020_RC04_h19(x):
        return  0.333[3]   +   x[7] * x[25] +   x[11] * x[26]  +   x[16] * x[34] +   x[19] * x[35]     # restricciones de igualdad de 50

    @staticmethod
    def CEC2020_RC04_h20(x):
        return  0.333[3]   +   x[7] * x[28] +   x[11] * x[29]  +   x[16] * x[37] +   x[19] * x[38]     # restricciones de igualdad de 30

    @staticmethod
    def CEC2020_RC04_h21(x):
        return x[21] + x[24] + x[27]      # restricciones de igualdad de 1

    @staticmethod
    def CEC2020_RC04_h22(x):
        return x[22] + x[25] + x[28]      # restricciones de igualdad de 1

    @staticmethod
    def CEC2020_RC04_h23(x):
        return x[23] + x[26] + x[29]      # restricciones de igualdad de 1

    @staticmethod
    def CEC2020_RC04_h24(x):
        return x[30] + x[33] + x[36]      # restricciones de igualdad de 1

    @staticmethod
    def CEC2020_RC04_h25(x):
        return x[31] + x[34] + x[37]      # restricciones de igualdad de 1

    @staticmethod
    def CEC2020_RC04_h26(x):
        return x[32] + x[35] + x[38]      # restricciones de igualdad de 1
    
    @staticmethod 
    def CEC2020_RC04_h27(x):
        return x[25] 
    
    @staticmethod
    def CEC2020_RC04_h28(x):
        return x[28]
    
    @staticmethod
    def CEC2020_RC04_h29(x):
       return x[23]
   
    @staticmethod
    def CEC2020_RC04_h30(x):
       return x[37]
   
    @staticmethod
    def CEC2020_RC04_h31(x):
       return x[32]
   
    @staticmethod
    def CEC2020_RC04_h32(x):
       return x[35] 

#********************************************************************************************************************************

#Problem 05

#********************************************************************************************************************************

#Problem 06

#********************************************************************************************************************************

#Problem 07

class CEC2020_RC07(Problem):
    
    # WITH BOUNDS:
    
    # 0 ≤ x1, ..., x20 ≤ 150; 0 ≤ x25, x27, x32, x35, x37, x29 ≤ 30;
    # 0 ≤ x21, x22, x23, x30, x33, x34, x36, x38, x39, x40, x42, x43, x44, x45, ≤ 1,
    # 0 ≤ x46, x47, x48 ≤ 1,
    # 0.85 ≤ x24, x26, x28, x31 ≤ 1

    
    SUPERIOR = np.array([
        150, 150, 150, 150, 150, 150, 150, 150, 150, 150,
        150, 150, 150, 150, 150, 150, 150, 150, 150, 150,
        1, 1, 1, 1, 30, 1, 30,
    ])
    INFERIOR = np.array([
        # 0 ≤ x1, ..., x20 ≤ 150
        0, 0, 0,    0, 0, 0, 0, 0, 0, 0,
        0, 0, 0,    0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0.85, 0, 0.85, 0, 
    ])

    def __init__(self):
        rest_h = [
            self.CEC2020_RC07_h1, self.CEC2020_RC07_h2, self.CEC2020_RC07_h3, self.CEC2020_RC07_h4,
            self.CEC2020_RC07_h5, self.CEC2020_RC07_h6, self.CEC2020_RC07_h7, self.CEC2020_RC07_h8,
            self.CEC2020_RC07_h9, self.CEC2020_RC07_h10, self.CEC2020_RC07_h11, self.CEC2020_RC07_h12,
            self.CEC2020_RC07_h13, self.CEC2020_RC07_h14, self.CEC2020_RC07_h15, self.CEC2020_RC07_h16,
            self.CEC2020_RC07_h17, self.CEC2020_RC07_h18, self.CEC2020_RC07_h19, self.CEC2020_RC07_h20,
            self.CEC2020_RC07_h21, self.CEC2020_RC07_h22, self.CEC2020_RC07_h23, self.CEC2020_RC07_h24,
            self.CEC2020_RC07_h25, self.CEC2020_RC07_h26, self.CEC2020_RC07_h27, self.CEC2020_RC07_h28,
            self.CEC2020_RC07_h29, self.CEC2020_RC07_h30, self.CEC2020_RC07_h31, self.CEC2020_RC07_h32,
            self.CEC2020_RC07_h33, self.CEC2020_RC07_h34, self.CEC2020_RC07_h35, self.CEC2020_RC07_h36,
            self.CEC2020_RC07_h37, self.CEC2020_RC07_h38, self.CEC2020_RC07_h39
        ]
        super().__init__(ProblemType.CONSTRAINED, self.SUPERIOR, self.INFERIOR, [],  rest_h)


    def fitness(self, individuo: np.array) -> float:
        
        x = np.copy(individuo)
                
        # Coeficientes de la función
        c = np.array([
            [0.23947, 0.758535],
            [-0.0139904, -0.0661588],
            [0.00955134, 0.0338147],
            [0.0077508, 0.0373349],
            [-0.0057719, 0.00163711],
            [0.0042656, 0.0286996]
        ])
    
        f_x = (
                c[0, 0] + (c[1, 0] + c[2, 0] * x[23] + c[3, 0] * x[37] + c[4, 0] * x[52] + c[5, 0] * x[44] + c[5, 0] * x[11]) +
                c[0, 1] + (c[1, 1] + c[2, 1] * x[25] + c[3, 1] * x[30] + c[4, 1] * x[37] + c[5, 1] * x[38] * x[12])
            )
        
        return f_x
    
    @staticmethod
    def CEC2020_RC07_h1(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h2(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h3(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h4(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h5(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h6(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h7(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h8(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h9(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h10(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h11(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h12(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h13(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h14(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h15(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h16(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h17(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h18(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h19(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0

    @staticmethod
    def CEC2020_RC07_h20(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h21(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h22(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h23(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h24(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h25(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h26(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h27(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h28(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h29(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h30(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h31(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h32(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h33(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h34(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h35(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h36(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h37(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h38(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0
    
    @staticmethod
    def CEC2020_RC07_h39(x):
        return x[0] - 10**4 * (x[6] - 100)  # restriccion 1 de igualdad = 0

#********************************************************************************************************************************

#Problem 02