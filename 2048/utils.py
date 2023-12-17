import numpy as np
import random

n_init_block = 2
new_values = [2, 4]

def init():
    table = np.zeros((4, 4), dtype=int)
    for i in range(n_init_block):
        x, y = random.randint(0, 3), random.randint(0, 3)
        v = random.sample(new_values, 1).pop()
        table[y][x] = v
    return table

def print_table(table):
    for i in range(4):
        print("-" * 32)
        row = ""
        for j in range(4):
            row += f"|  {table[i][j]}\t"
        row += "|"
        print(row)
    print("-" * 32)
    print("\n\n")