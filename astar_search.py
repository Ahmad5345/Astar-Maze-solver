from SearchSolution import SearchSolution
from heapq import heappush, heappop

from uninformed_search import backtrack


class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        # you write this part
        self.state = state
        self. heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        # you write this part
        return self.transition_cost +self.heuristic

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node, solution):
    current = node
    while current:
        solution.path.append(current.state)
        current = current.parent

    solution.path.reverse()
    return solution


def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_node = AstarNode(tuple(search_problem.start_state), heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {}
    visited_cost[start_node.state] = 0

    # you write the rest:
    while pqueue:
        current_node =  heappop(pqueue)
        solution.nodes_visited = solution.nodes_visited + 1
        solution.cost = solution.cost + current_node.transition_cost
        if current_node.state[1:] == search_problem.goal_locations[0:]:
            return backchain(current_node, solution)
        search_problem.maze.robotloc = list(current_node.state[1:])
        successors = search_problem.get_successors(current_node.state)

        for succ in successors:

            if succ == current_node.state:
                next_cost = 0
            else:
                next_cost = 1

            next_cost = next_cost + current_node.transition_cost
            succ_node = AstarNode(succ, heuristic_fn(succ), current_node, next_cost)

            if succ not in visited_cost or next_cost < visited_cost[succ]:
                visited_cost[succ] = next_cost
                heappush(pqueue, succ_node)

    return solution




