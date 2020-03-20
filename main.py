
#TODO test a* algo

import threading
import time
from board import Board
from a_star import AStar

R_C = 25 #Rows and Columns
W_H = 20 #Width and Height
start = (0,0)
goal = (24,24)
walls = []

cost = None
#path = []

board = Board("A*-Algorithm", R_C, R_C, W_H )

a_star = AStar(start, goal, R_C, R_C, walls)

def starThread():
    print("A* Thread started")
    global a_star, cost#, path
    cost = a_star.search()

def draw_path():
    #global a_star, board
    global board, a_star, cost
    board.draw()
    while cost == None:
        print("Drawing Thread started")
        board.draw_coordinates([a_tuple[1] for a_tuple in a_star.openlist.queue], "green")
        board.draw_coordinates(a_star.closedlist, "red")
        board.draw_coordinates(a_star.path, "black")
        
        board.draw_coordinates([start, goal], "yellow")

        board.platform.update()
        time.sleep(0.01)

    board.draw_coordinates([a_tuple[1] for a_tuple in a_star.openlist.queue], "green")
    board.draw_coordinates(a_star.closedlist, "red")
    if cost == -1:
        board.draw_coordinates(a_star.path, "orange")
        board.draw_coordinates([start, goal], "yellow")
    else:
        board.draw_coordinates(a_star.path, "black")

    board.platform.update()
    time.sleep(0.01)

t2 = threading.Thread(target=starThread)
t2.daemon = True
t2.start()
draw_path()
board.start()

