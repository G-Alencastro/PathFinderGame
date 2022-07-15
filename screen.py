import pygame 
from pygame.locals import *
from main import *
from grafics import plot_fit_mean
import matplotlib.pyplot as plt

    
pygame.init()

screen_size = (900, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('PathFinder')

fp = [850, 300]
pop = Population(300)
gen = 0

c = 0
clock = pygame.time.Clock()
while True:
    clock.tick(600)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    # if c < len(pop.individuals[0].genome):
    #     for i in range(len(pop.individuals)):
    #         pop.individuals[i].walk_a_step(pop.individuals[i].genome[c])
    #         pygame.draw.circle(screen, (100, 210, 50), (pop.individuals[i].pos[0], pop.individuals[i].pos[1]), 5, 1)
    #     c += 1
    # else:
    #     pop.fit_pop(fp)
    #     pop.new_population()
    #     gen += 1
    #     c = 0

    pop.pop_walk()
    pop.fit_pop(fp)
    pygame.draw.circle(screen, (100, 210, 50), (pop.individuals[0].pos[0], pop.individuals[0].pos[1]), 5, 1)
    pop.new_population()

    pygame.display.update()
