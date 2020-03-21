from board import Board
from math import floor
import random

class MapCreation:

    def __init__(self, R_C, W_H, board):
        self.walls = []
        self.start = None
        self.goal = None
        self.R_C = R_C
        self.W_H = W_H
        self.board = board
        board.platform.bind("<Button-1>", self.custom_map)
        board.platform.focus_set()

    def random_map(self):
        self.start = (random.randint(0, self.R_C-1), random.randint(0, self.R_C-1))
        self.goal = (random.randint(0, self.R_C-1), random.randint(0, self.R_C-1))
        for i in range(random.randint(0, (self.R_C*self.R_C))):
            wall = (random.randint(0, self.R_C-1), random.randint(0, self.R_C-1))
            if not wall == self.start and not wall == self.goal:
                if not wall in self.walls:
                    self.walls.append(wall)

    def custom_map(self, event):
        if not self.ready:
            item = self.board.platform.find_closest(event.x, event.y)[0]
            x = floor(event.x/self.W_H)
            y = floor(event.y/self.W_H)

            if self.start == None:
                self.start = (x, y)
                self.board.platform.itemconfig(item, fill='blue')
            elif self.goal == None:
                self.goal = (x, y)
                self.board.platform.itemconfig(item, fill='blue')
            elif self.start == (x,y):
                self.start = None
                self.board.platform.itemconfig(item, fill='white')
            elif self.goal == (x,y):
                self.goal = None
                self.board.platform.itemconfig(item, fill='white')
            elif (x, y) in self.walls:
                self.board.platform.itemconfig(item, fill='white')
                self.walls.remove((x, y))
            else:
                self.board.platform.itemconfig(item, fill='black')
                self.walls.append((x, y))
            self.board.platform.update()