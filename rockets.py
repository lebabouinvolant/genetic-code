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
        distance = self.position.distance_to(targetPoint)
        self.fitness = 1 / (distance+0.1) #éviter division par 0
    def reproduce(self, parent2, startingPos):
        child = Rocket(self.adn.length, self.adn.mutation_rate)
        child.adn = self.adn.reproduce(parent2.adn)
        child.position = startingPos.copy()
        return child
    def move(self, frame, dt):
        speedCoeff = 200
        XForce = (self.adn.genes[frame*2] - 0.5 ) * 2 *speedCoeff #On extrapole de 0 à 1 en -1 à 1
        YForce = (self.adn.genes[frame*2+1] - 0.5 ) * 2 *speedCoeff
        currentForce = pygame.Vector2(XForce, YForce)
        self.velocity += currentForce * dt
        self.position += self.velocity * dt
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, 1)

class RocketPopulation(gentools.Population):
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
simulationSpeed = 2
width, height = screen.get_size()
center = pygame.Vector2(width / 2, height / 2)
pop = RocketPopulation(30, Rocket, maxFrame*2, 0.01, center)
clock = pygame.time.Clock()
targetCoordinates = pygame.Vector2(random.randint(0, width), random.randint(0, height))
while run: #Une itération par génération
    while frame < maxFrame: #Une itération par frame
        clock.tick(60)
        for _ in range(simulationSpeed):
            pop.update(frame, SIM_DT)
            frame += 1
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), targetCoordinates, 10)

        pop.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pop.select(targetCoordinates)
    frame = 0

pygame.quit()
