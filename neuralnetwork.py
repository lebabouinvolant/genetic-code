import random

class Perceptron():
    """
    Les poids vont de -1 à 1 et sont chacun associés à un input. Le Perceptron de base consiste en 3 poids et 2 inputs (plus 1 de biais qui vaut tjrs 1 et qui est associé au poids de biais)
    """
    def __init__(self, n):
        self.weights = []
        for _ in range(n): self.weights.append((random.random()-0.5)*2)
    def neuron(self, inputs):
        sum = 0
        for i in range(2):
            sum += self.weights[i] * inputs[i]
        return sum
    def activate(self, val):
        if val < 0:
            return -1
        return 1
    def feedForward(self, inputs):
        return self.activate(self.neuron(inputs))
    def train(self, inputs, desired):
        output = self.feedForward(inputs)
        error = desired-output
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i]

def f(x):
    return 3*x+7

def run(neuron):
    for _ in range(2000):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        desired = 1
        if f(x) > y:
            desired = -1 
        neuron.train([x, y, 1], desired)

def test(neuron):
    good = 0
    cnt = 0 
    for _ in range(100):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        desired = 1
        if f(x) > y:
            desired = -1 
        if neuron.feedForward([x, y, 1]) == desired:
            good += 1
        cnt += 1
    print(f"Le modèle a eu bon dans {good} / {cnt} cas")


perceptron = Perceptron(3)
run(perceptron)
test(perceptron)