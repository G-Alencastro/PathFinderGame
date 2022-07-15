import matplotlib.pyplot as plt
from random import randint

def plot_fit_mean(gen, mf):

    plt.xlabel('Generations')
    plt.ylabel('Mean Fitness')
    plt.title('Mean of fitness in function of generations')
    plt.plot(gen, mf, color='black')
    plt.pause(1)

