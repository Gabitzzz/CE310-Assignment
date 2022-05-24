import random

population_size = 20000
generations = 30
src_domain = (-1.25, 1.25)
mtn = 0.05
crs = 0.8
pop_list = []

def init_population():
    for i in range(population_size):
        new_population = (
        random.uniform(src_domain[0], src_domain[1]), random.uniform(src_domain[0], src_domain[1]))
        pop_list.append(new_population)


def max_fitness():
    max_f = -1000
    for i in range(len(pop_list)):
        curent_fit = fitness(pop_list[i])
        if max_f < curent_fit:
            max_f = curent_fit
    return max_f


def crossover(p1, p2):
    rnd_cross = random.random()
    c1 = p1[0] * rnd_cross + p2[0] * (1 - rnd_cross)
    rnd_cross = random.random()
    c2 = p1[1] * rnd_cross + p2[1] * (1 - rnd_cross)
    return (c1, c2)


def mutation(value):
    v1 = value[0] + (random.uniform(-0.1, 0.1))
    v2 = value[1] + (random.uniform(-0.1, 0.1))

    if v1 > src_domain[1]:
        v1 = src_domain[1]
    elif v1 < src_domain[0]:
        v1 = src_domain[0]
    if v2 > src_domain[1]:
        v2 = src_domain[1]
    elif v2 < src_domain[0]:
        v2 = src_domain[0]
    return (v1, v2)


def tournament(participants=4, boolean=False):
    max_fit = -10000
    min_fit = 10000

    for i in range(participants):
        current_i = random.randint(0, len(pop_list) - 1)
        curent_fit = fitness(pop_list[current_i])
        if boolean == False:
            if min_fit > curent_fit:
                out_of_bound = current_i
                min_fit = curent_fit

        else:
            if max_fit <= curent_fit:
                out_of_bound = current_i
                max_fit = curent_fit
    return out_of_bound


import math
import numpy as np


def Simionescu(x, y):
    return 0.1 * x * y


def fitness(value):
    x, y = value
    var = (x ** 2 + y ** 2 - (1 + 0.2 * math.cos(8 * np.arctan(x / y))) ** 2) ** 2
    return -(Simionescu(x, y) + 2 * var)


init_population()

for i in range(generations):
  for value in range(population_size):
    if random.random()>crs:
      offspring = pop_list[tournament()]
    else:
      p1 = pop_list[tournament()]
      p2 = pop_list[tournament()]
      offspring = crossover(p1, p2)
    if random.random()>mtn:
      offspring = mutation(offspring)
    pop_list[tournament(boolean=True)] = offspring
  if i%1==0:
    max_f = max_fitness()
    print("Generation {}: Max fitness: {}, population[]: {}".format(i,max_f,pop_list[0]))

print('Final Fitness: ',max_fitness())