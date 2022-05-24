import random


##create population
def create_population(destinations, population_numb):
    population = []  # list for storing the population

    # initial population
    for i in range(population_numb):
        population.append("".join(random.choice('01') for it in range(destinations)))
    return population


def crossover(chrom1, chrom2):
    cut_point = random.randint(1, destinations - 2)  # select random point for cut
    offspring = chrom1[0:cut_point] + chrom2[cut_point:]
    return offspring


##mutation
def bit_flip_mutation(chromosome):
    chrom_length = len(chromosome)
    for i in range(chrom_length):  # for each bit
        if random.random() <= mutation_rate:  # if random number is smaller than set mutation rate
            list_c = list(chromosome)  # converts to list to allow bit flip
            if list_c[i] == "0":
                list_c[i] = "1"
            else:
                list_c[i] = "0"
            chromosome = "".join(list_c)  # rejoins into string
        return (chromosome)


# main algorithm
def GA(population):
    for g in range(generations):  # for each generation
        fit = []
        for i in range(population_numb):
            # population fitness
            fit.append(fitness(population[i]))

        print('\n')
        print("Current Generation: " + str(g + 1))
        count = 0
        for p in population:
            print(p + " -- " + str(fit[count]))
            count += 1

        index = sorted(range(len(fit)), key=lambda k: fit[k], reverse=True)  ##indexes and sorts population

        population_new = []
        for i in index[:select_numb]:
            population_new.append(population[i])

        for i in range(select_numb, population_numb):  ##for remainder of population
            parents = random.sample(range(0, select_numb - 1),
                                    2)  ##selects 2 random parents (can not be the same parent twice)
            offspring = crossover(population_new[parents[0]],
                                            population_new[parents[1]])  ##performs crossover
            offspring = bit_flip_mutation(offspring)  ##performs mutation
            population_new.append(offspring)

        population = population_new  ##resets the population to the new population

    fit = []
    for i in range(population_numb):
        fit.append(fitness(population[i]))

    index = sorted(range(len(fit)), key=lambda k: fit[k], reverse=True)  ##indexes and sorts population
    return population[index[0]]


import random

population_numb = 10  # population size
select_numb = 5  # number to progress to next generation
generations = 20  # number of generations
mutation_rate = 0.01  # mutation rate
budget = 5000  # total money
destinations = 30  # how many destinations
cost = []

for i in range(destinations):
    cost.append(random.randint(100, 500))  # random list of prices

# create population
population = create_population(destinations, population_numb)


# fitness function

def fitness(chromosome):
    total_cost = 0
    for i in range(len(chromosome)):
        if chromosome[i] == "1":
            total_cost += cost[i]
    if (total_cost > budget):
        fit = 0
    else:
        fit = total_cost
    return fit


# run GA
chromosome = GA(population)

print("\nBest individual: " + chromosome)

total_dest = 0
total_cost = 0
for i in range(len(chromosome)):
    if chromosome[i] == "1":
        total_cost += cost[i]
        total_dest += 1

print("You can go to " + str(total_dest) + " places for £" + str(total_cost))










