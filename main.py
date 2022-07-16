from random import randint
import matplotlib.pyplot as plt
from grafics import plot_fit_mean


class Individual:
    def __init__(self,genome_length=500, screen_size=(900, 600)):
        self.genome = [randint(0, 3) for _ in range(genome_length)]
        self.fit = 0
        self.screen_size = screen_size
        self.pos = [10, 300]

    def get_fit(self, final_number):
        distance = ((self.pos[0]-final_number[0])**2)**0.5
        max_dis = final_number[0]
        fit = max_dis-distance
        self.fit = fit
        return fit

    def walk_a_step(self, gen, step_size=5):
        if gen == 0 and self.pos[0] < self.screen_size[0]:
            self.pos[0] += step_size
            return
        if gen == 1 and self.pos[0] > 5:
            self.pos[0] -= step_size
            return
        if gen == 2 and self.pos[1] < self.screen_size[1]:
            self.pos[1] += step_size
            return
        if gen == 3 and self.pos[1] > 5:
            self.pos[1] -= step_size

class Population:
    def __init__(self, n_ind, genome_length=500):
        self.n_ind = n_ind
        self.individuals = [Individual(genome_length) for _ in range(n_ind)]
        self.mean_fit = 0

    def pop_walk(self):
        for c in range(len(self.individuals[0].genome)):
            for i in range(self.n_ind):
                self.individuals[i].walk_a_step(self.individuals[i].genome[c])

    def fit_pop(self, f_num):
            # get mean fit of population
            for ind in self.individuals:
                self.mean_fit += ind.get_fit(f_num)
            self.mean_fit /= self.n_ind


            # sorting the population by fitness
            changed = True
            while changed:
                changed = False
                for c in range(1, self.n_ind):
                    if self.individuals[c].fit > self.individuals[c-1].fit:
                        self.individuals[c], self.individuals[c-1] = self.individuals[c-1], self.individuals[c]
                        changed = True

    def new_population(self):
        def crossover(fathers):
            father_genome_len = len(fathers[0].genome)
            new_ind01 = Individual(father_genome_len)
            new_ind02 = Individual(father_genome_len)

            new_genome01 = []
            new_genome02 = []

            for c in range(father_genome_len):
                decisor_num = randint(0,1)
                if decisor_num:
                    new_genome01.append(fathers[0].genome[c])
                    new_genome02.append(fathers[1].genome[c])
                else:
                    new_genome01.append(fathers[1].genome[c])
                    new_genome02.append(fathers[0].genome[c])


            new_ind01.genome = new_genome01
            new_ind02.genome = new_genome02

            return new_ind01, new_ind02

        def mutation(ind, mut_tax=1):
            for c in range(len(ind.genome)):
                mut = randint(0, 100)
                if mut <= mut_tax:
                    ind.genome[c] = randint(0, 3)       

        def choose_father():
            ag_fit = 0
            ag_fit_list = []
            for ind in self.individuals:
                ag_fit += ind.fit
                ag_fit_list.append(ag_fit)
            
            chosen_num = randint(0, int(ag_fit))
            for c in range(self.n_ind-1):
                if ag_fit_list[c] < chosen_num < ag_fit_list[c+1]:
                    return self.individuals[c]
            return self.individuals[0]

        new_inds = []
        for _ in range(self.n_ind//2):
            father01, father02 = choose_father(), choose_father()
            son01, son02 = crossover([father01, father02])
            mutation(son01)
            mutation(son02)
            new_inds.append(son01)
            new_inds.append(son02)

        self.individuals = new_inds
        self.mean_fit = 0


if  __name__ == '__main__':
    fp = [850, 300]
    pop = Population(500)
    gen = 0
    for c in range(100):
        pop.pop_walk()
        pop.fit_pop(fp)
        plot_fit_mean(gen, pop.mean_fit)
        pop.new_population()
        gen += 1