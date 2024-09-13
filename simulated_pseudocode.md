```python
Initialize the board with a random configuration of queens
Set an initial temperature T
While T > T_min:
    Select a neighboring solution
    If the neighbor has a lower number of conflicts:
        Move to the neighbor solution
    Else:
        Move to the neighbor with a probability exp(-delta_conflicts / T)
    Reduce the temperature T
If a solution with no conflicts is found:
    Return the solution
Else:
    Return the best found solution

```
