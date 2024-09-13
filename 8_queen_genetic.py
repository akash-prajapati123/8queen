#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

# Configuration
POPULATION_SIZE = 200
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.9
MAX_GENERATIONS = 5000
BOARD_SIZE = 8

class Individual:
    def __init__(self, chromosome=None):
        if chromosome is None:
            self.chromosome = [random.randint(0, BOARD_SIZE - 1) for _ in range(BOARD_SIZE)]
        else:
            self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        conflicts = 0
        for i in range(BOARD_SIZE):
            for j in range(i + 1, BOARD_SIZE):
                if self.chromosome[i] == self.chromosome[j]:
                    conflicts += 1
                if abs(self.chromosome[i] - self.chromosome[j]) == abs(i - j):
                    conflicts += 1
        return BOARD_SIZE * (BOARD_SIZE - 1) // 2 - conflicts

    def mate(self, partner):
        crossover_point = random.randint(0, BOARD_SIZE - 1)
        child_chromosome = self.chromosome[:crossover_point] + partner.chromosome[crossover_point:]
        return Individual(child_chromosome)

    def mutate(self):
        if random.random() < MUTATION_RATE:
            row = random.randint(0, BOARD_SIZE - 1)
            self.chromosome[row] = random.randint(0, BOARD_SIZE - 1)
            self.fitness = self.calculate_fitness()

def roulette_wheel_selection(population):
    total_fitness = sum(ind.fitness for ind in population)
    selection_point = random.uniform(0, total_fitness)
    running_sum = 0

    for individual in population:
        running_sum += individual.fitness
        if running_sum > selection_point:
            return individual

def genetic_algorithm():
    population = [Individual() for _ in range(POPULATION_SIZE)]

    best_fitness = population[0].fitness
    stagnant_generations = 0

    for generation in range(MAX_GENERATIONS):
        population = sorted(population, key=lambda x: x.fitness, reverse=True)
        
        if population[0].fitness == BOARD_SIZE * (BOARD_SIZE - 1) // 2:
            print(f"Solution found in generation {generation}")
            return population[0]

        if population[0].fitness > best_fitness:
            best_fitness = population[0].fitness
            stagnant_generations = 0
        else:
            stagnant_generations += 1

        if stagnant_generations > 500:
            print(f"Stagnating... stopping after {generation} generations")
            break

        new_population = population[:20]

        while len(new_population) < POPULATION_SIZE:
            parent1 = roulette_wheel_selection(population)
            parent2 = roulette_wheel_selection(population)

            if random.random() < CROSSOVER_RATE:
                child = parent1.mate(parent2)
            else:
                child = parent1

            child.mutate()
            new_population.append(child)

        population = new_population

    print("No solution found.")
    return None

if __name__ == "__main__":
    solution = genetic_algorithm()
    if solution:
        print("Solution:", solution.chromosome)

