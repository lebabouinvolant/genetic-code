import random

class Matrix():
    def __init__(self, PARAMETER): 
        """Parameter peut être soit un tuple de 2 nombres (le nb de lignes et de colonnes de la matrice) soit un tableau de nombres à 2 dimensions qui sert de modèle"""
        if type(PARAMETER) == type([]):
            self.representation = PARAMETER
            self.lines = len(PARAMETER)
            self.columns = len(PARAMETER[0])
        elif type(PARAMETER) == type(()):
            self.lines = PARAMETER[0]
            self.columns = PARAMETER[1]
            self.representation = [[0 for _ in range(self.columns)] for _ in range(self.lines)]
        else:
            raise Exception("L'argument passé à la méthode d'initialisation n'est pas correct (tuple de 2 éléments ou tableau 2D)")
    def multiply(self, OTHER) -> Matrix:
        """Cette fonction renvoie le produit d'une matrice par un scalaire ou une autre matrice
        Elle prend en argument soit un nombre, auquel cas la matrice sera multipliée par un scalaire, soit une matrice, auquel cas on fera un produit matriciel"""
        if type(OTHER) == Matrix:
            return self.multiplybymatrix(OTHER)
        else:
            return self.multiplybyscalar(OTHER)
    def multiplybymatrix(self, otherMatrix: Matrix) -> Matrix:
        """Fonction renvoyant le produit de 2 matrices et prenant en argument la matrice à multiplier avec l'instance de classe"""
        if self.columns != otherMatrix.lines:
            raise Exception("Les 2 matrices ne sont pas compatibles pour un produit") #Multiplication impossible
        output = Matrix([[0 for _ in range(otherMatrix.columns)] for _ in range(self.lines)]) #Nouvelle matrice de taille 
        for i in range(self.lines):
            for j in range(otherMatrix.columns):
                val = 0
                for k in range(self.columns):
                    val += self.representation[i][k] * otherMatrix.representation[k][j]
                output[i][j] = val
        return output
    def multiplybyscalar(self, scalar) -> Matrix:
        output = Matrix([[0 for _ in range(self.columns)] for _ in range(self.lines)])
        for i in range(self.lines):
            for j in range(self.columns):
                output.representation[i][j] = self.representation[i][j] * scalar
        return output
    def sum(self, otherMatrix: Matrix) -> Matrix:
        """Somme de 2 matrices de même dimension"""
        if self.columns != otherMatrix.columns or self.lines != otherMatrix.lines:
            raise Exception("Les 2 matrices ne sont pas compatibles pour une somme")
        output = Matrix((self.lines, self.columns))
        for i in range(self.lines):
            for j in range(self.columns):
                output.representation[i][j] = self.representation[i][j] + otherMatrix[i][j]
        
        return output
    def sub(self, otherMatrix: Matrix) -> Matrix:
        """Somme de 2 matrices de même dimension"""
        if self.columns != otherMatrix.columns or self.lines != otherMatrix.lines:
            raise Exception("Les 2 matrices ne sont pas compatibles pour une somme")
        output = Matrix([[0 for _ in range(self.columns)] for _ in range(self.lines)])
        for i in range(self.lines):
            for j in range(self.columns):
                output = self.representation[i][j] - otherMatrix[i][j]
        return output
    def randomize(self) -> None:
        for i in range(self.lines):
            for j in range(self.columns):
                self.representation[i][j] = (random.random()-0.5) * 2 

    def assign(self, target: list):
        """Cette méthode permet d'assigner la matrice à une nouvelle représentation"""
        self.representation = target
        self.lines = len(target)
        self.columns = len(target[0])
    def transpose(self):
        output = Matrix((self.columns,self.lines))
        for i in range(self.lines):
            for j in range(self.columns):
                output[j][i] = self.representation[j][i]
    def map(self, func: function):
        for el in self.representation:
            for el2 in el:
                el2 = func(el2)
    def bilan(self):
        out = 0
        for el in self.representation:
            for el2 in el:
                out += el2
        return out
    def __add__(self, other: Matrix) -> Matrix:
        """Somme de 2 matrices de même dimension"""
        return self.sum(other)
    def __sub__(self, other: Matrix) -> Matrix:
        """Différence de 2 matrices de même dimension"""
        return self.sub(other)
    def __getitem__(self, key):
        """Récupérer les valeurs contenues dans la matrices (utilise l'attribut sous jacent representation)"""
        return self.representation[key]
    def __mul__(self, other) -> Matrix:
        """Multiplie une matrice soit par un scalaire soit par une autre matrice compatible"""
        return self.multiply(other)
    def __repr__(self) -> str:
        rep = ""
        for el in self.representation:
            rep += str(el) + "\n"
        return rep
    def __str__(self) -> str:
        return str(self.representation)
    def __len__(self) -> int:
        return len(self.representation)