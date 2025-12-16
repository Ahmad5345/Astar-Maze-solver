
from collections import deque
from re import search

#from FoxProblem import FoxProblem
from SearchSolution import SearchSolution

# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions

def bfs_search(search_problem):

    start = SearchNode(search_problem.start_state)
    visited = set()
    queue = deque([start])
    flag = False

    while queue:
        node = queue.popleft()
        if node.state not in visited:
            visited.add(node.state)
            if search_problem.goal_test(node.state):
                flag = True
                backtrack(node)
                break
            for i in search_problem.get_successors(node.state):
                if i not in visited:
                    queue.append(SearchNode(i, node))

    return flag

def backtrack(node):
    count = 1
    print(count)
    while node.parent is not None:
        count = count + 1
        print(count)
        node = node.parent



# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")

    # you write this part
    return dfs(node, set(), search_problem, 0, depth_limit)



def dfs(node, current_path, search_problem, curr_depth, limit):
    if search_problem.goal_test(node.state):
        backtrack(node)
        return 0
    if limit < curr_depth:
        return 1

    current_path.add(node.state)

    for i in search_problem.get_successors(node.state):
        if i not in current_path:
            answer = dfs(SearchNode(i, node), current_path, search_problem, curr_depth+1, limit)
            if answer == 1 or answer == 0:
                return answer

    current_path.remove(node.state)

    return 2






def ids_search(search_problem, depth_limit=18):
    node = SearchNode(search_problem.start_state)
    solution = SearchSolution(search_problem, "DFS")
    i = 0
    while i <= depth_limit:
        answer = dfs_search(search_problem, i, node)
        if answer == 0:
            break
        i = i + 1
