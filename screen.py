import pygame 
from pygame.locals import *
from main import *
from grafics import plot_fit_mean
import matplotlib.pyplot as plt
from random import randint


pygame.init()

screen_size = (900, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('PathFinder')

fp = [850, 300]
pop = Population(200)
gen = 0
c = 0

fst_ln_x, lst_ln_x = 0, 0
fst_ln_y, lst_ln_y = 900, 0

fps = 60
clock = pygame.time.Clock()
while True:
    clock.tick(fps)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                fps += 50
            if event.key == K_DOWN:
                fps -= 50
        if event.type == QUIT:
            pygame.quit()

    pygame.draw.rect(screen, (250, 250, 200), ((fst_ln_x, fst_ln_y), (lst_ln_x-fst_ln_x, lst_ln_y-fst_ln_y)))
    pygame.draw.circle(screen, (250, 10, 10), fp, 10)

    if c < len(pop.individuals[0].genome):
        for i in range(len(pop.individuals)):
            pop.individuals[i].walk_a_step(pop.individuals[i].genome[c])
            if gen > 0:
                pygame.draw.circle(screen, (100, randint(100, 250), 100), (pop.individuals[i].pos[0], pop.individuals[i].pos[1]), 5, 2)

        c += 1
    else:
        pop.fit_pop(fp)
        fst_ln_x, lst_ln_x = 850, 0
        fst_ln_y, lst_ln_y = 850, 0
        for ind in pop.individuals:
            fst_ln_y = ind.pos[1] if ind.pos[1] < fst_ln_y else fst_ln_y
            lst_ln_y = ind.pos[1] if ind.pos[1] > lst_ln_y else lst_ln_y
            
            fst_ln_x = ind.pos[0] if ind.pos[0] < fst_ln_x else fst_ln_x
            lst_ln_x = ind.pos[0] if ind.pos[0] > lst_ln_x else lst_ln_x
        
        print(gen, pop.mean_fit)
        pop.new_population()
        gen += 1
        c = 0

    # pop.pop_walk()
    # pop.fit_pop(fp)
    # print(pop.individuals[0].genome.count(0))
    # pygame.draw.circle(screen, (100, 210, 50), (pop.individuals[0].pos[0], pop.individuals[0].pos[1]), 5, 1)
    # pop.new_population()

    pygame.display.update()
