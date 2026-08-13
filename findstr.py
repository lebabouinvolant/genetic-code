import random
import string
import math
import gentools
mutation_rate = 0.01
numberOfConcurents = 150


class Phrase():
    def adnToString(self):
        self.phrase = ''.join(chr((math.floor(n * 26)) + ord('a') - 1) for n in self.adn.genes)
    def __init__(self, length, mutation):
        self.adn = gentools.ADN(length, mutation)
        self.fitness = 0
        self.adnToString()
    def evaluate(self, target):
        score = 0
        for i in range(len(self.phrase)):
            if self.phrase[i] == target[i]:
                score += 1
        self.fitness = score / len(self.phrase)
    def reproduce(self, parent2):
        child = Phrase(self.adn.length, self.adn.mutation_rate)
        child.adn = self.adn.reproduce(parent2.adn)
        child.adnToString()
        return child
        

obj = "lebabouinvolant"


def main():
    population = []
    for i in range(numberOfConcurents):
        population.append(Phrase(len(obj), mutation_rate))
    success = False
    cnt = 0
    while success == False:
        for el in population:
            el.evaluate(obj)
            if(el.fitness == 1): success = True; break
        matingpool = []
        for el in population:
            n = math.floor(el.fitness * 100)
            for _ in range(n): matingpool.append(el)
        for i in range(len(population)):
            parent1 = random.choice(matingpool)
            parent2 = random.choice(matingpool)
            population[i] = parent1.reproduce(parent2)
        cnt += 1
        print(f"Génération {cnt}, un mot présent est {population[0].phrase}")
    print(f"Objectif atteint en {cnt} générations!")



if __name__ == "__main__": main()