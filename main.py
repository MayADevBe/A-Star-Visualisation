
#TODO test board (drawing)
#TODO test a* algo

import threading
from board import Board
from a_star import AStar

R_C = 25 #Rows and Columns
W_H = 20 #Width and Height
start = (0,0)
goal = (5,10)
walls = []

cost = 0
path = []

board = Board("A*-Algorithm", R_C, R_C, W_H )

a_star = AStar(start, goal, W_H , W_H , walls)

def starThread():
    print("A* Thread started")
    global a_star, cost
    cost = a_star.search()
    if not cost == None:
        path = a_star.get_path()
        print(f"Path: {path}")
    else:
        path = [start]
        print("No Path")
    return path

def draw_path(board, path):
     #global a_star, board
     print("Drawing Thread started")
     print(f"Draw_Path {a_star.openlist.queue}")
     print(f"Draw_Path {[a_tuple[1] for a_tuple in a_star.openlist.queue]}")
     print(f"Draw_Path {a_star.closedlist}")
     board.draw_coordinates([a_tuple[1] for a_tuple in a_star.openlist.queue], "green")
     board.draw_coordinates(a_star.closedlist, "red")
     board.draw_coordinates(path, "black")

# t = threading.Thread(target=starThread)
# t.daemon = True
# t2 = threading.Thread(target=draw_path)
# t2.daemon = True
# t.start()
# t2.start()
path = starThread()
#draw_path(path)
board.start(draw_path, path)
