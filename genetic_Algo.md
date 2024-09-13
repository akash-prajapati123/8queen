```python
Genetic Algorithm
The Genetic Algorithm (GA) is a metaheuristic inspired by the process of natural selection. It belongs to the larger class of evolutionary algorithms (EA), which generate solutions to optimization and search problems using techniques inspired by natural evolution, such as mutation, crossover, and selection.

The steps for the Genetic Algorithm are as follows:

Initialization: Randomly generate a population of candidate solutions (chromosomes).
Fitness Function: Evaluate how "good" each candidate solution is.
Selection: Choose better solutions from the population for reproduction.
Crossover: Combine two parent solutions to generate offspring.
Mutation: Randomly alter some parts of a candidate solution to maintain genetic diversity.
Termination: Stop if the algorithm finds an optimal solution or reaches a predefined number of generations.
Algorithm
Representation of Chromosome:

Each chromosome represents a possible solution to the 8-Queens problem.
A chromosome is an 8-element list, where the index represents the row number, and the value at each index represents the column position of the queen in that row.
Fitness Function:

The fitness function evaluates how many queens are attacking each other.
The fewer the number of conflicts, the better the solution. An optimal solution will have zero conflicts.
Selection:

Use Tournament Selection or Roulette Wheel Selection to choose parent chromosomes based on their fitness.
Crossover:

Apply Single Point Crossover. Select a point along the chromosome and swap parts of two parent chromosomes to produce offspring.
Mutation:

Randomly mutate a gene (i.e., change the column of a queen in a random row).
Termination:

The algorithm stops when a solution is found (no conflicts) or after a fixed number of generations.


```
