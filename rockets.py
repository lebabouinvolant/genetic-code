import gentools
import math
import pygame
import random

class Rocket():
    def __init__(self, length, mutation, pos=pygame.Vector2(0,0)):
        self.adn = gentools.ADN(length, mutation)
        self.fitness = 0
        self.position = pos.copy()
        self.velocity = pygame.Vector2(0, 0)
    def evaluate(self, targetPoint):
        score = self.position - targetPoint
        self.fitness = 1 / score
    def reproduce(self, parent2):
        child = Rocket(self.adn.length, self.adn.mutation_rate)
        child.adn = self.adn.reproduce(parent2.adn)
        return child
    def move(self, frame, dt):
        speedCoeff = 300
        XForce = (self.adn.genes[frame*2] - 0.5 ) * 2 *300 #On extrapole de 0 à 1 en -1 à 1
        YForce = (self.adn.genes[frame*2+1] - 0.5 ) * 2 *300
        currentForce = pygame.Vector2(XForce, YForce)
        self.velocity += currentForce * dt
        self.position += self.velocity * dt
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, 1)



class Population():
    def __init__(self, numberOfRockets, length, mutation, pos):
        self.population = []
        for _ in range(numberOfRockets):
            self.population.append(Rocket(length, mutation, pos))
    def select(self, target):
        mating_pool = []
        for el in self.population:
            el.evaluate(target)
            for _ in range(el.score):
                mating_pool.append(el)
        for i in range(len(self.population)):
            parent1 = random.choice(mating_pool)
            parent2 = random.choice(mating_pool)
            self.population[i] = parent1.reproduce(parent2)
    def update(self, frame, dt):
        for el in self.population:
            el.move(frame, dt)
    def draw(self, screen):
        for el in self.population:
            el.draw(screen)
    

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Genetic Rockets")


run = True
frame = 0
maxFrame = 300
SIM_DT = 1 / 60
width, height = screen.get_size()
center = pygame.Vector2(width / 2, height / 2)
pop = Population(30, maxFrame*2, 0.01, center)
clock = pygame.time.Clock()
targetCoordinates = pygame.Vector2(random.randrange(0, width), random.randrange(0, height))
while run and frame < maxFrame:
    clock.tick(60)
    pop.update(frame, SIM_DT)
    frame += 1
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), targetCoordinates, 10)

    pop.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

pygame.quit()
