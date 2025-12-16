import tkinter as tk
from time import sleep

from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search

name = "maze8.maz"

# Initialize the main window
root = tk.Tk()
root.title("Sensorless Problem")

win_label = tk.Label(root, text="Path Completed!", font=("Helvetica", 24), fg="green")
win_label.pack(pady=20)
win_label.pack_forget()

main_screen = tk.Frame(root)
main_screen.pack()

welcome_label = tk.Label(main_screen, text="Welcome to the Sensorless Robot Problem!", font=("Helvetica", 24))
welcome_label.pack(pady=20)

miss_label = tk.Label(main_screen, text="Input Goal State:", font=("Helvetica", 14))
miss_label.pack(pady=5)
miss_entry = tk.Entry(main_screen)
miss_entry.pack(pady=5)

cann_label = tk.Label(main_screen, text="Input Start location:", font=("Helvetica", 14))
cann_label.pack(pady=5)
cann_entry = tk.Entry(main_screen)
cann_entry.pack(pady=5)

def separate_input_values(input_value):
    try:
        # Split the input by comma and convert to integers
        x, y = map(int, input_value.split(','))
        return x,y
    except ValueError:
        error_label = tk.Label(root, text="Please enter the coordinates in 'x,y' format.", font=("Helvetica", 24), fg="red")
        error_label.pack(pady=20)
        root.mainloop()
        exit()


def create_grid(root, width, height):
    cells = []  # List to hold references to the cells

    for row in range(height):
        root.grid_rowconfigure(row, weight=1)  # Make each row expandable
    for col in range(width):
        root.grid_columnconfigure(col, weight=1)  # Make each column expandable

    for row in range(height):
        row_cells = []  # List for cells in the current row
        for col in range(width):
            color = 'white'
            cell = tk.Label(root, borderwidth=1, relief="solid", bg=color, width=10, height=5)
            cell.grid(row=row, column=col, sticky="nsew")
            row_cells.append(cell)  # Add cell to the row list
        cells.append(row_cells)  # Add the row list to the main list

    return cells  # Return the list of cells

def change_colors(cells, row, col, new_color):
    cells[col][row].config(bg=new_color)

def start_game():
    main_screen.forget()
    input1 = separate_input_values(miss_entry.get())
    input2 = separate_input_values(cann_entry.get())
    test_maze3 = Maze(name)
    test_mp = SensorlessProblem(test_maze3, (input1[0], input1[1]))
    solution = astar_search(test_mp, test_mp.super_manhattan_heuristic)

    lose_label = tk.Label(root, text="NO SOLUTION", font=("Helvetica", 24), fg="red")
    lose_label.pack(pady=20)
    if len(solution.path) > 0:
        lose_label.pack_forget()

    cells = create_grid(root, test_maze3.width, test_maze3.height)
    change_colors(cells, input2[0], test_maze3.height - input2[1] - 1, "blue")

    for y in range(test_maze3.height):
        for x in range(test_maze3.width):
            if not test_maze3.is_floor(x,y):
                change_colors(cells, x, test_maze3.height-y-1, "red")
    my_list = list(input2)
    for i in solution.path:
        setx = 0
        sety = 0
        if i[0] == 0:
            setx = 1
        else:
            if i[0] == 1:
                setx = -1
            else:
                if i[0] == 2:
                    sety = -1
                else:
                    if i[0] == 3:
                        sety = 1
        if test_maze3.is_floor(my_list[0] + setx, my_list[1] + sety) and i[0] != -1:
            my_list[0] = my_list[0] + setx
            my_list[1] = my_list[1] + sety
            change_colors(cells, my_list[0], test_maze3.height - my_list[1] - 1, "green")
    change_colors(cells, input1[0], test_maze3.height - input1[1] - 1, "orange")
    change_colors(cells, input2[0], test_maze3.height - input2[1] - 1, "blue")



start_button = tk.Button(main_screen, text="Animate Path", command=start_game)
start_button.pack(pady=20)

root.mainloop()
