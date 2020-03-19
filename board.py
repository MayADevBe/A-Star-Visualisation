import tkinter as tk

class Board:
    '''Creates GUI Board'''

    def __init__(self, title, rows, columns, width):
        self.window = tk.Tk()
        self.window.title(title)
        self.width = width
        self.columns = columns
        self.rows = rows
        self.platform = tk.Canvas(self.window, width = columns*width, height = rows*width)
        self.platform.pack()

    def draw(self):
        for i in range(self.columns):
            for j in range(self.rows):
                self.platform.create_rectangle(i*self.width, j*self.width, (i+1)*self.width, (j+1)*self.width, fill="white")
        
    def draw_coordinates(self, coordinate_list, color):
        for i, j in coordinate_list:
            self.platform.create_rectangle(i*self.width, j*self.width, (i+1)*self.width, (j+1)*self.width, fill=color)

    def start(self, drawfunc, path):
        self.draw()
        drawfunc(self, path)
        self.window.mainloop()

# R_C = 25 #Rows and Columns
# W_H = 20 #Width and Height
# board = Board("Test", R_C, R_C, W_H)

# board.start()
