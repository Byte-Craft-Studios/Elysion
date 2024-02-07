from pathfinding.core.grid import Grid 
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

matrix = [
    [1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1]]

# create a grid
grid = Grid(matrix = matrix)

# create a start and end cell
start = grid.node(0, 0)         # x and y (topleft)
end = grid.node(5,2)            # x and y (last line, last column)

# create a finder with a movement style 
finder = AStarFinder(diagonal_movement = DiagonalMovement.always)

# use the finder to find the path
path, runs = finder.find_path(start, end, grid)

# print result
print(path)
print(runs)