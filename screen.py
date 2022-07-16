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
pop = Population(500)
gen = 0

c = 0

fst_ln_x, lst_ln_x = 0, 0

clock = pygame.time.Clock()
while True:
    clock.tick(600)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.draw.circle(screen, (250, 10, 10), fp, 10)
    pygame.draw.rect(screen, (180, 190, 250), ((fst_ln_x, 0), (10, screen_size[1])))
    pygame.draw.rect(screen, (250, 250, 90), ((lst_ln_x, 0), (10, screen_size[1])))

    if c < len(pop.individuals[0].genome):
        for i in range(len(pop.individuals)):
            pop.individuals[i].walk_a_step(pop.individuals[i].genome[c])
            if gen%1 == 0:
                pygame.draw.circle(screen, (80, 150, 50), (pop.individuals[i].pos[0], pop.individuals[i].pos[1]), 5, 2)

        c += 1
    else:
        pop.fit_pop(fp)
        fst_ln_x = pop.individuals[0].pos[0]
        lst_ln_x = pop.individuals[-1].pos[0]
        pop.new_population()
        print(gen)
        gen += 1
        c = 0

    # pop.pop_walk()
    # pop.fit_pop(fp)
    # print(pop.individuals[0].genome.count(0))
    # pygame.draw.circle(screen, (100, 210, 50), (pop.individuals[0].pos[0], pop.individuals[0].pos[1]), 5, 1)
    # pop.new_population()

    pygame.display.update()
