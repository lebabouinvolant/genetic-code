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
    """
    Classe utilitaire pour les populations de "crÃ©atures" exploitant le systÃ¨me d'ADN implÃ©mentÃ© ci-dessus.
    Le dernier argument (additionalArgs) doit Ãªtre un tableau qui contient tous les arguments passÃ©s Ã  chaque instance de crÃ©ature de toutes les gÃ©nÃ©rations, gÃ©nÃ©ralement pour contenter leur logique mÃ©tier (par exemple la position de dÃ©part des crÃ©atures)
    """
    def __init__(self, numberOfElements, ElementType, length, mutation):
        self.population = []
        for _ in range(numberOfElements):
            self.population.append(ElementType(length, mutation))
    def select(self, target=None):
        newPopulation = []
        for el in self.population:
            if target: el.evaluate(target)
            else: el.evaluate()
        for _ in range(len(self.population)):
            parent1 = self.weightedSelection()
            parent2 = self.weightedSelection()
            newPopulation.append(parent1.reproduce(parent2))
        self.population = newPopulation
    def weightedSelection(self):
        totalFitness = sum(el.fitness for el in self.population)
        idx = 0
        start = random.random()*totalFitness
        while start > 0:
            start -= self.population[idx].fitness
            idx += 1
        return self.population[idx-1]