import random

class ADN():
    def __init__(self, length, mutation_rate):
        self.genes = [random.random() for _ in range(length)]
        self.length = length
        self.mutation_rate = mutation_rate
    def reproduce(self, parent2):
        child = ADN(self.length, self.mutation_rate)
        for i in range(self.length):
            if random.random() < 0.5:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = parent2.genes[i]
        child.mutate()
        return child
    def mutate(self):
        for i in range(self.length):
            if random.random() < self.mutation_rate:
                self.genes[i] = random.random()

class Population():
    def __init__(self, numberOfElements, ElementType, length, mutation, pos):
        self.population = []
        self.startingPos = pos.copy()
        for _ in range(numberOfElements):
            self.population.append(ElementType(length, mutation, pos))
    def select(self, target):
        totalFitness = 0
        newPopulation = []
        for el in self.population:
            el.evaluate(target)
        for i in range(len(self.population)):
            parent1 = self.weightedSelection()
            parent2 = self.weightedSelection()
            newPopulation.append(parent1.reproduce(parent2, self.startingPos))
        self.population = newPopulation
    def weightedSelection(self):
        totalFitness = sum(el.fitness for el in self.population)
        idx = 0
        start = random.random()*totalFitness
        while start > 0:
            start -= self.population[idx].fitness
            idx += 1
        return self.population[idx-1]
