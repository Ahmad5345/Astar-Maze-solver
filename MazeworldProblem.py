from time import sleep

from Maze import Maze

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        self.start_state = (0,) + tuple(maze.robotloc)


    def __str__(self):
        string =  "Mazeworld problem: "
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


    def get_successors(self, current):
        x = current[current[0]*2+1]
        y = current[current[0]*2+2]
        robo_number = len(self.maze.robotloc)/2
        successors = set()
        successors.add(self.find_successors(list(current), x, y, robo_number))
        if self.check_safe(x+1, y):
            successors.add(self.find_successors(list(current), x+1, y, robo_number))

        if self.check_safe(x-1, y):
            successors.add(self.find_successors(list(current), x-1, y, robo_number))

        if self.check_safe(x, y+1):
            successors.add(self.find_successors(list(current), x, y+1, robo_number))

        if self.check_safe(x, y-1):
            successors.add(self.find_successors(list(current), x, y-1, robo_number))

        return successors


    def find_successors(self, curr_list, x, y, robo_number):
        curr_list[curr_list[0]*2+1] = x
        curr_list[curr_list[0]*2+2] = y
        curr_list[0] = (int)((curr_list[0] + 1) % robo_number)
        return tuple(curr_list)


    def check_safe(self, x, y):
        number = (self.maze.width * (self.maze.height - 1 - y)) + x
        if number < 0 or number >= len(self.maze.create_render_list()) or not self.maze.is_floor(x,y):
            return False
        return self.maze.create_render_list()[number] == "."


    def manhattan_heuristic(self, state):
        robots = (int)(len(state)/2)
        answer = 0
        for i in range(robots):
            answer = answer + (abs(self.goal_locations[i*2]-state[i*2+1]) + abs(self.goal_locations[i*2+1]-state[i*2+2]))
        return answer





## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((1, 1, 0, 1, 1, 2, 1)))

