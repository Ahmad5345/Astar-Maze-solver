from Maze import Maze
from time import sleep

class SensorlessProblem:

    ## You write the good stuff here:

    def __init__(self, maze, goal_locations=(0,0)):
        self.goal_locations = goal_locations
        self.maze = maze
        self.start_state = (-1,)
        for y in range(maze.height):
            for x in range(maze.width):
                if maze.is_floor(x, y):
                    self.start_state = self.start_state + (x, y)

    def __str__(self):
        string =  "Blind robot problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))

    def get_successors(self, state):
        Mainsuc = set()
        for i in range(4):
            succ = (i,)
            check = set()
            setx = 0
            sety = 0
            if i == 0:
                setx = 1
            else:
                if i == 1:
                    setx = -1
                else:
                    if i == 2:
                        sety = -1
                    else:
                        if i == 3:
                            sety = 1
            for j in range(1, len(state),2):
                if self.maze.is_floor(state[j]+setx, state[j+1]+sety):
                    if (state[j]+setx, state[j+1]+sety) not in check:
                        succ = succ + (state[j]+setx, state[j+1]+sety,)
                        check.add((state[j]+setx, state[j+1]+sety,))
                else:
                    succ = succ + (state[j], state[j+1],)
                    check.add((state[j], state[j+1],))
            Mainsuc.add(succ)

        return Mainsuc

    def super_manhattan_heuristic(self, state):
        answer = 0
        for j in range(1, len(state),2):
            answer = answer + abs(self.goal_locations[0]-state[j]) + abs(self.goal_locations[1]-state[j+1])
        return answer




    




## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze0.maz")
    test_problem = SensorlessProblem(test_maze3)
