from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search

# Test problems

test_maze3 = Maze("maze1.maz")
test_mp = SensorlessProblem(test_maze3, (1,0))

# this should do a bit better:
result = astar_search(test_mp, test_mp.super_manhattan_heuristic)
test_mp.animate_path(result.path)

# Your additional tests here:
# You write this:
test_maze1 = Maze("maze1.maz")
test_mp = SensorlessProblem(test_maze1, (2,2))
result = astar_search(test_mp, test_mp.super_manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze2 = Maze("maze2.maz")
test_mp = SensorlessProblem(test_maze2, (7,0))
result = astar_search(test_mp, test_mp.super_manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze4 = Maze("maze4.maz")
test_mp = SensorlessProblem(test_maze4, (6, 1))
result = astar_search(test_mp, test_mp.super_manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze5 = Maze("maze5.maz")
test_mp = SensorlessProblem(test_maze5, (2, 0))
result = astar_search(test_mp, test_mp.super_manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze6 = Maze("maze6.maz")
test_mp = SensorlessProblem(test_maze6, (1, 0))
result = astar_search(test_mp, test_mp.super_manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze7 = Maze("maze7.maz")
test_mp = SensorlessProblem(test_maze7, (0, 0))
result = astar_search(test_mp, test_mp.super_manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze8 = Maze("maze8.maz")
test_mp = SensorlessProblem(test_maze8, (39, 9))
result = astar_search(test_mp, test_mp.super_manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)
