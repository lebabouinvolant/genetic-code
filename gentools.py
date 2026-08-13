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
