
#TODO test a* algo

import threading
from board import Board
from a_star import AStar

R_C = 25 #Rows and Columns
W_H = 20 #Width and Height
start = (0,0)
goal = (20,20)
walls = []

cost = None
#path = []

board = Board("A*-Algorithm", R_C, R_C, W_H )

a_star = AStar(start, goal, W_H , W_H , walls)

def starThread():
    print("A* Thread started")
    global a_star, cost#, path
    cost = a_star.search()
    # if not cost == None:
    #     path = a_star.get_path()
    #     print(f"Path: {path}")
    # else:
    #     path = [start]
    #     print("No Path")
    #return path

def draw_path():
    #global a_star, board
    global board, a_star, cost
    board.draw()
    while cost == None:
        print("Drawing Thread started")
        print(f"Draw_Path {a_star.openlist.queue}")
        print(f"Draw_Path {[a_tuple[1] for a_tuple in a_star.openlist.queue]}")
        print(f"Draw_Path {a_star.closedlist}")
        board.draw_coordinates([a_tuple[1] for a_tuple in a_star.openlist.queue], "green")
        board.draw_coordinates(a_star.closedlist, "red")
        board.draw_coordinates(a_star.path, "black")
        
        board.draw_coordinates([start, goal], "yellow")

        board.platform.update()

t2 = threading.Thread(target=starThread)
t2.daemon = True
t2.start()
draw_path()
#starThread()
board.start()

