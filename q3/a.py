import math

with open("input.txt") as file:
    grid = [[char for char in line] for line in file.read().split("\n") if line]


def tree_count(grid, x, y):
    """ n trees encountered stepping x right and y down in each step"""

    width = len(grid[0])
    steps = math.ceil(len(grid) / y)
    return sum([grid[i * y][(i * x) % width] == "#" for i in range(steps)])

# Part 1
print(tree_count(grid, 3, 1))

# Part 2
print(
    tree_count(grid, 1, 1)
    * tree_count(grid, 3, 1)
    * tree_count(grid, 5, 1)
    * tree_count(grid, 7, 1)
    * tree_count(grid, 1, 2)
)
