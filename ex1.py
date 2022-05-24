
import random
pop = []


path = "/Users/gabitzzz/ce310.txt"

# read file
with open(path, 'r') as file:
    Binary = file.read().replace('\n', '')

# HYPER-PARAMETERS
bits_numb = len(Binary)
population_numb = 30   # population number

select_numb = 11  # number of selects
generation_numb = 20    # generations number
rate = 0.02  # mutation rate between 0 and 1

# create population
population = (bits_numb, population_numb)


# define fitness function
def fitness(parent):
    score = 0
    counter = 0
    # counter for each binary bit
    for c in parent:
        if c == Binary[counter]:
            score += 1
        counter += 1
    return score

# run GA
# result = GA(population)


def GA(population):
    # iterate each generation
    for g in range(population_numb):
        fitness_values = []
        # check fitness for all population
        for i in range(population_numb):
            fitness_values.append(fitness(pop[i]))

        print("Generation #" + str(g + 1))
        count = 0

        index = sorted(range(len(fitness_values)), key=lambda k: fitness_values[k], reverse=True)

        new_population = []
        # select top values
        for i in index[:select_numb]:
            new_population.append(pop[i])

        # creating new iteration, generation, crossover and mutation
        for i in range(select_numb, population_numb):
            # 2 random unique parents are selected
            parents = random.sample(range(0, select_numb - 1), 2)
            # crossover function used
            child = crossover(new_population[parents[0]],
                              new_population[parents[1]])
            # mutation function is used
            child = mutation(child)
            new_population.append(child)

        # sets population for next iteration, generation, crossover and mutation
        pop = new_population

    # fitness for last generation
    fitness_values = []
    for i in range(population_numb):
        fitness_values.append(fitness(pop[i]))

    # sorts population and return best parent
    index = sorted(range(len(fitness_values)), key=lambda k: fitness_values[k], reverse=True)
    return pop[index[0]]


result = GA(population)

with open(path, 'r') as file:
    Binary = file.read()

position = Binary.find('\n')

lines = []
for i in range(0, len(result), (position)):
    lines.append(result[i:i + (position)])

print("\nRESULT:")
print('\n'.join(lines))




# create population
def create_pop(bits_numb, pop_numb):
    # create a list to store the population
    pop = []
    # create random list to fill population with random binary
    for i in range(pop_numb):
        pop.append("".join(random.choice('01') for it in range(bits_numb)))
    return pop

#mutation
def mutation(value):
    for i in range(len(value)):  # for each individual
        # rate -> mutation rate
        if random.random() <= rate:  # if smaller than rate
            temp = list(value)  # convert to list
            if temp[i] == "0":
                temp[i] = "1"
            else:
                temp[i] = "0"
            value = "".join(temp)
        return (value)

# crossover function
def crossover(p1, p2):
    point = random.randint(1, bits_numb - 2)  # select random point for cut
    child = p1[0:point] + p2[point:]
    return child






