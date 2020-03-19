
#TODO test board (drawing)
#TODO test a* algo

import threading
from board import Board
from a_star import AStar

R_C = 25 #Rows and Columns
W_H = 20 #Width and Height
start = (0,0)
goal = (1,1)
walls = []

cost = 0
path = []

board = Board("A*-Algorithm", R_C, R_C, W_H )

a_star = AStar(start, goal, W_H , W_H , walls)

def starThread():
    print("A* Thread started")
    global a_star, cost, path
    cost = a_star.search()
    print(cost)
    path = a_star.get_path()
    print(path)

def draw_path():
     global path, a_star, board
     print("Drawing Thread started")
     board.draw_coordinates(a_star.openlist, "green")
     board.draw_coordinates(a_star.closedlist, "red")
     board.draw_coordinates(path, "black")

t = threading.Thread(target=starThread)
t.daemon = True
t2 = threading.Thread(target=draw_path)
t2.daemon = True
board.start()