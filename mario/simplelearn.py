"""
Ce script implémente l'entrainement d'agents par RL sur mario 1, avant de montrer le jeu du meilleur agent au final.
"""




import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import gentools
import gymnasium as gym
import gym_super_mario_bros
import numpy as np
import math
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT


class Player():
    """
    La classe reprÃ©sentant un joueur. chaque valeur de l'ADN explicite un input parmi les 4 possibles: 0-0.25 pour rien, 0.25-50 pour droite, 0.50-0.75 pour gauche et 0.75-1 pour saut
    """
    def __init__(self, length, mutation, env=None):
        self.adn = gentools.ADN(length, mutation)
        self.fitness = 0
        self.totalSteps = 0
    def setEnv(self, env=None):
        if env == None:
            self.env = gym.make("SuperMarioBros-v0")
            self.env = JoypadSpace(self.env, SIMPLE_MOVEMENT)
        else: self.env = env
        self.env.reset()

    def step(self, playIdx):
        self.totalSteps += 1
        action = math.floor(self.adn.genes[playIdx] * 4)
        next_state, reward, done, trunc, info = self.env.step(action)
        if done or trunc:
            self.env.reset()
        self.fitness += (reward + 15)/30 #Reward est comprise entre -15 et 15 donc on normalise tt Ã§a
    def reproduce(self, parent2):
        child = Player(self.adn.length, self.adn.mutation_rate)
        child.adn = self.adn.reproduce(parent2.adn)
        return child
    def evaluate(self):
        self.fitness = self.fitness / self.totalSteps

class PlayerPopulation(gentools.Population):
    def __init__(self, numberOfElements, length, mutation):
        self.nbSteps = length
        super().__init__(numberOfElements, Player, length, mutation)
        for el in self.population: el.setEnv() 
    def play(self):
        for i in range(self.nbSteps):
            for el in self.population:
                el.step(i)
    def select(self, target=None):
        allEnvs = []
        for el in self.population:
            allEnvs.append(el.env)
        super().select(target)
        for i in range(len(self.population)):
            self.population[i].setEnv(allEnvs[i])

playersPop = PlayerPopulation(10, 200, 0.01)
for epoch in range(5):
    playersPop.play()
    playersPop.select()


showableplayer = playersPop.population[0]
import time

env = gym.make("SuperMarioBros-v0", render_mode="human")
env = JoypadSpace(env, SIMPLE_MOVEMENT)

env.reset()

for el in showableplayer.adn.genes:
    action = math.floor(el * 4)
    env.step(action)
    env.render()
    time.sleep(0.1)

time.sleep(5)
env.close()