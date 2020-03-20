import threading
import time
import random
from board import Board
from a_star import AStar

R_C = 25 #Rows and Columns
W_H = 20 #Width and Height
start = (0,0)
goal = (24,24)
walls = []

cost = None

def random_search():
    global start, end, walls
    start = (random.randint(0, R_C-1), random.randint(0, R_C-1))
    end = (random.randint(0, R_C-1), random.randint(0, R_C-1))
    for i in range(random.randint(0, (R_C*R_C))):
        wall = (random.randint(0, R_C-1), random.randint(0, R_C-1))
        if not wall == start and not wall == goal:
            if not wall in walls:
                walls.append(wall)

def starThread():
    global a_star, cost#, path
    cost = a_star.search()

def draw_path():
    global board, a_star, cost, walls
    board.draw()
    while cost == None:
        board.draw_coordinates([a_tuple[1] for a_tuple in a_star.openlist.queue], "green")
        board.draw_coordinates(a_star.closedlist, "yellow")
        board.draw_coordinates(a_star.path, "orange")
        
        board.draw_coordinates(walls, "black")
        board.draw_coordinates([start, goal], "blue")

        board.platform.update()
        time.sleep(0.01)

    board.draw_coordinates([a_tuple[1] for a_tuple in a_star.openlist.queue], "green")
    board.draw_coordinates(a_star.closedlist, "yellow")
    board.draw_coordinates(walls, "black")
    if cost == -1:
        board.draw_coordinates(a_star.path, "red")
        board.draw_coordinates([start, goal], "blue")
    else:
        board.draw_coordinates(a_star.path, "blue")

    board.platform.update()
    time.sleep(0.01)

board = Board("A*-Algorithm", R_C, R_C, W_H )

random_search()
a_star = AStar(start, goal, R_C, R_C, walls)

t2 = threading.Thread(target=starThread)
t2.daemon = True
t2.start()
draw_path()
board.start()

