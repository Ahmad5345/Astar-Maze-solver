from MazeworldProblem import MazeworldProblem
from Maze import Maze

from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

# Your additional tests here:
test_maze1 = Maze("maze1.maz")
test_mp = MazeworldProblem(test_maze1, (3,0))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze2 = Maze("maze2.maz")
test_mp = MazeworldProblem(test_maze2, (7,2))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze4 = Maze("maze4.maz")
test_mp = MazeworldProblem(test_maze4, (6, 0 ,6, 1, 5, 1))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze5 = Maze("maze5.maz")
test_mp = MazeworldProblem(test_maze5, (1, 0 ,0, 0, 2, 0))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze6 = Maze("maze6.maz")
test_mp = MazeworldProblem(test_maze6, (1, 0 ,2, 0, 0, 0))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze7 = Maze("maze7.maz")
test_mp = MazeworldProblem(test_maze7, (1, 0 ,2, 0, 0, 0))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze8 = Maze("maze8.maz")
test_mp = MazeworldProblem(test_maze8, (39, 9 ,38, 9, 37, 9))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze0 = Maze("maze0.maz")
test_mp = MazeworldProblem(test_maze0, (6,5,6,6,6,7))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)
