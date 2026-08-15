import random


class NeuralNetwork():
    """La classe de base pour un réseau de neurone, la fonction d'initialisation prend les nombres d'inputs, de neurones cachés et d'outputs en entrée
    Pour l'instant c'est un réseau 3 couches et fully connected, on passera au deep learning plus tard
    On initialise les poids entre -1 et 1"""
    def __init__(self, ninputs, nhiddens, noutputs):
        self.inputnumber = ninputs
        self.hiddens = Matrix([
            [(random.random()-0.5) * 2 for _ in range(ninputs)] for _ in range(nhiddens)
        ])

        self.outputs = [(random.random()-0.5) * 2 for _ in range(noutputs)]
    def feedForward(self, inputs):
        for neuron in self.hiddens:
            neuron.feedForward()

class Matrix(): #Ne suppporte que des matrices de dimension 2 max actuellement, et la matrice par défaut est en 2*2
    def __init__(self, lines=2, columns=2, modelArray=None):
        if modelArray != None:
            self.representation = modelArray
            self.lines = len(modelArray)
            self.columns = len(modelArray[0])
        else:
            self.lines = lines
            self.columns = columns
            self.representation = [[0 for _ in range(columns)] for _ in range(lines)]
    def multiplybymatrix(self, otherMatrix: Matrix):
        """Fonction renvoyant le produit de 2 matrices et prenant en argument la matrice à multiplier avec l'instance de classe"""
        if self.columns != otherMatrix.lines:
            raise Exception("Les 2 matrices ne sont pas compatibles pour un produit") #Multiplication impossible
        output = [[0 for _ in range(otherMatrix.columns)] for _ in range(self.lines)] #Nouvelle matrice de taille 
        for i in range(self.lines):
            for j in range(otherMatrix.columns):
                val = 0
                for k in range(self.columns):
                    val += self.representation[i][k] * otherMatrix.representation[k][j]
                output[i][j] = val
        return output

        
    def multiplybyscalar(self, scalar):
        for el in self.representation:
            for el2 in el:
                el2 *= scalar
    def sum(self, otherMatrix: Matrix):
        if self.columns != otherMatrix.columns or self.lines != otherMatrix.lines:
            raise Exception("Les 2 matrices ne sont pas compatibles pour une somme") #Multiplication impossible
        for i in range(self.lines):
            for j in range(self.columns):
                self.representation[i][j] += otherMatrix[i][j]

m1 = Matrix(0, 0, [[1, 2], [3, 5]])
m2 = Matrix(0, 0, [[10, 8, 7], [13, 11, 8]])
print(m1.multiplybymatrix(m2))