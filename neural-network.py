import random
from matrix import Matrix
import math
class NeuralNetwork():
    """La classe de base pour un réseau de neurone, la fonction d'initialisation prend les nombres d'inputs, de neurones cachés et d'outputs en entrée
    Pour l'instant c'est un réseau 3 couches et fully connected, on passera au deep learning plus tard
    On initialise les poids entre -1 et 1"""
    def __init__(self, ninputs, nhiddens, noutputs, nhiddenlayers = 1):
        """L'initialisation de la classe NeuralNetwork prend 3 arguments: le nombre d'entrées du réseau, le nombre de neurones de la couche cachée et le nombre de sorties  """
        self.inputnumber = ninputs
        self.neurons = [Matrix((nhiddens, ninputs))] #self.neurons[couche][neurone][poids(autrement dit index du précédent neurone qui est connecté par ce poids)] La première hidden layer doit prendre les inputs en entrée, contrairement aux suivantes
        for _ in range(nhiddenlayers-1):
            self.neurons.append(Matrix((nhiddens, nhiddens)))
        self.neurons.append(Matrix((noutputs, nhiddens))) # The output layer
        self.biases = [Matrix((nhiddens, 1)) for _ in range(nhiddenlayers)]
        self.biases.append(Matrix((noutputs, 1))) #Output bias
        for el in self.neurons:
            el.randomize()
        for el in self.biases:
            el.randomize()
    def feedForward(self, inputs: Matrix):
        """
        La fonction responsable de faire fonctionner le réseau de neurone.
        Elle prend un argument: les inputs (sous forme d'une matrice de n*1)
        """
        processed = inputs
        for i in range(len(self.neurons)):
            processed = self.neurons[i] * processed
            processed += self.biases[i]
            processed.map(self.sigmoid) #Activation
        return processed
    def feedForTrain(self, inputs : Matrix):
        """
        Similaire à feedForward sauf qu'elle renvoie aussi les outputs intermédiaires
        """
        processed = inputs
        intermediates = []
        for i in range(len(self.neurons)):
            processed = self.neurons[i] * processed
            processed += self.biases[i]
            intermediates.append([processed]) #The actual values
            processed.map(self.sigmoid) #Activation
            intermediates[i].append(processed) #Activated values
        return processed, intermediates

    def train(self, input, answer):
        """
        La fonction responsable d'entraîner le réseau de neurone avec un input et un output donné.
        Les inputs et les outputs doivent être donnés sous forme de matrices (de la même taille que prévus par le réseau, cela va de soi)
        """
        result, intermediates = self.feedForTrain(input)
        errors = [(result[i][0]-answer[i][0])**2 for i in range(len(result))]
        lastlayer = len(self.neurons)-1
        cost = sum(errors)/len(errors) #Le coût est la moyenne des erreurs
        deltas = [[0 for _ in range(len(self.neurons[i]))] for i in range(len(self.neurons))] #On y stocke les dérivées des neurones (somme des connections): 1 élément par neurone, cela fait aussi office de gradient du biais
        weightgradient = [[[0 for _ in range(len(self.neurons[i][j]))] for j in range(len(self.neurons[i]))] for i in range(len(self.neurons))] #On y stocke les dérivées des poids (1 élément par connection)
        for i in range(len(self.neurons[lastlayer])): #Pour chaque neurone de la dernière couche
            outputderivated = (2 / len(self.neurons[lastlayer])) * (intermediates[lastlayer][i][1] - answer[i][0]) #A quel point changer l'output va changer le coût (qui est égal à la moyenne des erreurs)
            activationderivated = intermediates[lastlayer][i][1] * (1-intermediates[lastlayer][i][1]) #Formule pour la fonction sigmoïde
            deltas[lastlayer][i] = outputderivated * activationderivated
            for j in range((len(self.neurons[lastlayer][i]))): #Pour chaque poids
                weightgradient[lastlayer][i][j] = deltas[lastlayer][i] * intermediates[lastlayer-1][j][1] #delta de ce neurone fois activation de celui auquel relie le poids
        for i in range(len(self.neurons)-2, -1, -1): #Pour chaque couche en descendant (sauf la couche d'output)
            for j in range(len(self.neurons[i])): #Pour chaque neurone
                errorDerivated = 0
                for neuronIndex in range(len(deltas[i+1])): #On somme tous les deltas des neurones suivants fois les poids qui les relient au neurone actuel pour trouver le gradient d'activation du neurone actuel par rapport à la valeur activée du neurone
                    errorDerivated += deltas[i+1][neuronIndex] * self.neurons[i+1][neuronIndex][j]
                deltas[i][j] = intermediates[i][j][1] * (1-intermediates[i][j][1]) * errorDerivated
                for k in range(len(self.neurons[i][j])): #Pour chaque connection appartenant à un neurone
                    if i == 0: #On doit aller chercher non pas la valeur activée du neurone précédent mais l'input
                        weightgradient[i][j][k] = deltas[i][j] * input[k][0]
                    else: weightgradient[i][j][k] = deltas[i][j] * intermediates[i-1][k][1]
        for i in range(len(self.neurons)):
            for j in range(len(self.neurons[i])):
                for k in range(len(self.neurons[i][j])):
                    self.neurons[i][j][k] = weightgradient[i][j][k] #Update weights
                self.biases[i][j] = deltas[i][j] #Update biases
    @staticmethod 
    def sigmoid(x):
        return 1/(1+math.e**-x)
    

test = NeuralNetwork(1, 5, 3, 3)
print(test.feedForTrain(Matrix([[1]])))