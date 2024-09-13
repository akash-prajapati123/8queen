#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import math

# Configuration
BOARD_SIZE = 8
INITIAL_TEMPERATURE = 10000
FINAL_TEMPERATURE = 0.001
COOLING_RATE = 0.995
MOVES_PER_TEMPERATURE = 100

class Board:
    def __init__(self):
        self.queens = [random.randint(0, BOARD_SIZE - 1) for _ in range(BOARD_SIZE)]
        self.conflicts = self.calculate_conflicts()

    def calculate_conflicts(self):
        """Calculates the number of conflicts between queens."""
        conflicts = 0
        for i in range(BOARD_SIZE):
            for j in range(i + 1, BOARD_SIZE):
                if self.queens[i] == self.queens[j]:
                    conflicts += 1
                if abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def make_move(self):
        """Generate a neighboring solution by moving a queen involved in conflicts."""
        row = random.choice([i for i in range(BOARD_SIZE) if self.is_in_conflict(i)])
        new_column = random.randint(0, BOARD_SIZE - 1)
        while new_column == self.queens[row]:
            new_column = random.randint(0, BOARD_SIZE - 1)

        new_queens = self.queens[:]
        new_queens[row] = new_column
        return BoardWithMove(new_queens)

    def is_in_conflict(self, row):
        """Check if a queen is in conflict."""
        for j in range(BOARD_SIZE):
            if row != j:
                if self.queens[row] == self.queens[j] or abs(self.queens[row] - self.queens[j]) == abs(row - j):
                    return True
        return False

    def set_board(self, queens):
        self.queens = queens
        self.conflicts = self.calculate_conflicts()

class BoardWithMove(Board):
    def __init__(self, queens):
        self.queens = queens
        self.conflicts = self.calculate_conflicts()

def acceptance_probability(current_conflicts, new_conflicts, temperature):
    """Calculate the probability of accepting a worse solution."""
    if new_conflicts < current_conflicts:
        return 1.0
    return math.exp((current_conflicts - new_conflicts) / temperature)

def simulated_annealing():
    board = Board()
    temperature = INITIAL_TEMPERATURE

    while temperature > FINAL_TEMPERATURE:
        for _ in range(MOVES_PER_TEMPERATURE):
            if board.conflicts == 0:
                print("Solution found!")
                return board.queens

            new_board = board.make_move()

            if acceptance_probability(board.conflicts, new_board.conflicts, temperature) > random.random():
                board.set_board(new_board.queens)

        temperature *= COOLING_RATE

        if temperature <= FINAL_TEMPERATURE and board.conflicts > 0:
            print("Restarting with a new random configuration.")
            board = Board()  # Restart with a new random board
            temperature = INITIAL_TEMPERATURE  # Reset temperature

    print("No optimal solution found.")
    return board.queens

if __name__ == "__main__":
    solution = simulated_annealing()
    print("Final board configuration:", solution)

