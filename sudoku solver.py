import tkinter as tk
from tkinter import messagebox

def is_valid_move(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False
    
    for y in range(9):
        if grid[y][col] == number:
            return False
        
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == number:
                return False

    return True

def find_empty_locations(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(grid):
    empty_pos = find_empty_locations(grid)
    if not empty_pos:
        return True             # Puzzle solved
    
    row, col = empty_pos

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    
    return False

def print_grid(grid):
    for row in range(len(grid)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(len(grid[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(grid[row][col])
            else:
                print(str(grid[row][col]) + " ", end="")

# Initial Sudoku Grid
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],    
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# GUI Implementation
class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()
        self.set_initial_values()

    def create_widgets(self):
        frame = tk.Frame(self.master)
        frame.pack()
        
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(frame, width=5, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col)
                self.entries[row][col] = entry
                
                if (row // 3 + col // 3) % 2 == 1:
                    entry.configure(bg="#e0e0e0")
        
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=20)
        
        solve_button = tk.Button(button_frame, text="Solve", command=self.solve, width=10, bg="#d3d3d3", font=('Arial', 14))
        solve_button.grid(row=0, column=0, padx=5)
        
        clear_button = tk.Button(button_frame, text="Clear", command=self.clear, width=10, bg="#d3d3d3", font=('Arial', 14))
        clear_button.grid(row=0, column=1, padx=5)

    def set_initial_values(self):
        for row in range(9):
            for col in range(9):
                if sudoku_grid[row][col] != 0:
                    self.entries[row][col].insert(0, str(sudoku_grid[row][col]))
                    self.entries[row][col].configure(state='disabled')
                    self.grid[row][col] = sudoku_grid[row][col]

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.entries[row][col]['state'] != 'disabled':
                    val = self.entries[row][col].get()
                    if val.isdigit():
                        self.grid[row][col] = int(val)
                    else:
                        self.grid[row][col] = 0

        if solve_sudoku(self.grid):
            for row in range(9):
                for col in range(9):
                    if self.entries[row][col]['state'] != 'disabled':
                        self.entries[row][col].delete(0, tk.END)
                        self.entries[row][col].insert(0, str(self.grid[row][col]))
        else:
            messagebox.showinfo("Sudoku Solver", "No solution found")

    def clear(self):
        for row in range(9):
            for col in range(9):
                if self.entries[row][col]['state'] != 'disabled':
                    self.entries[row][col].delete(0, tk.END)
                    self.grid[row][col] = 0

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
