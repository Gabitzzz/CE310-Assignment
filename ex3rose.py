import random

population_size = 20000
search_domain = (-1.5, 1.5)
p_mutation = 0.05
p_crossover = 0.8
generation = 45
pop = []


def init_opulation():
    for i in range(population_size):
        new_population = (
        random.uniform(search_domain[0], search_domain[1]), random.uniform(search_domain[0], search_domain[1]))
        pop.append(new_population)


def max_fitness():
    max_fit = -1000
    for i in range(len(pop)):
        f_i = fitness(pop[i])
        if max_fit < f_i:
            max_fit = f_i
    return max_fit


def crossover(p1, p2):
    croos = random.random()
    v1 = p1[0] * croos + p2[0] * (1 - croos)
    croos = random.random()
    v2 = p1[1] * croos + p2[1] * (1 - croos)
    return (v1, v2)


def mutation(individual):
    x = individual[0] + (random.uniform(-0.2, 0.2))
    y = individual[1] + (random.uniform(-0.2, 0.2))

    if x < search_domain[0]:
        x = search_domain[0]
    elif x > search_domain[1]:
         x = search_domain[1]

    if y < search_domain[0]:
        y = search_domain[0]
    elif y > search_domain[1]:
        y = search_domain[1]
    return (x, y)

def tournament(participants=4, boolean=False):
    fit_max = -10000
    fit_min = 10000

    for i in range(participants):
        index = random.randint(0, len(pop) - 1)
        f_i = fitness(pop[index])
        if boolean == False:
            if fit_max <= f_i:
                out_index = index
                fit_max = f_i
        else:
            if fit_min > f_i:
                out_index = index
                fit_min = f_i
    return out_index

#


def Rosenbrock(x,y):
  return (1-x)**2 + 100*(y-x**2)**2

def fitness(individual):
  x,y = individual
  penalty = (x**2 + y**2 -2)**2
  return -(Rosenbrock(x,y) + 2* penalty)

#
init_opulation()

for i in range(generation):
  for individual in range(population_size):
    if random.random()>p_crossover:
      ofspring = pop[tournament()]
    else:
      p1 = pop[tournament()]
      p2 = pop[tournament()]
      ofspring = crossover(p1, p2)
    if random.random()>p_mutation:
      ofspring = mutation(ofspring)
    pop[tournament(boolean=True)] = ofspring
  if i%1==0:
    max_f = max_fitness()
    print("Gen {}: \n Max fitness: {} \n Population: {}".format(i,max_f,pop[0]))
    print('\n')

print('Final Fitness: ',max_fitness())