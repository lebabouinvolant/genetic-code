import random
from matrix import Matrix
class NeuralNetwork():
    """La classe de base pour un réseau de neurone, la fonction d'initialisation prend les nombres d'inputs, de neurones cachés et d'outputs en entrée
    Pour l'instant c'est un réseau 3 couches et fully connected, on passera au deep learning plus tard
    On initialise les poids entre -1 et 1"""
    def __init__(self, ninputs, nhiddens, noutputs):
        """L'initialisation de la classe NeuralNetwork prend 3 arguments: le nombre d'entrées du réseau, le nombre de neurones de la c  """
        self.inputnumber = ninputs
        self.hiddens = Matrix([
            [(random.random()-0.5) * 2 for _ in range(ninputs)] for _ in range(nhiddens)
        ])

        self.outputs = Matrix([[(random.random()-0.5) * 2 for _ in range(nhiddens)] for _ in range(noutputs)])
    def feedForward(self, inputs: Matrix):
        """
        La fonction responsable de faire fonctionner le réseau de neurone.
        Elle prend un argument: les inputs (sous forme d'une matrice de n*1)
        """
        processed = self.hiddens * inputs
        output = self.outputs * processed
        return output
    def activate():
        pass
        

test = NeuralNetwork(1, 5, 3)
print(test.feedForward(Matrix([[1]])))