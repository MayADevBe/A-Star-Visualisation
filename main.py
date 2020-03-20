import threading
import time
from board import Board
from a_star import AStar
from create_map import MapCreation

R_C = 25 #Rows and Columns
W_H = 20 #Width and Height

cost = None

def star_thread():
    global a_star, cost#, path
    cost = a_star.search()

def creation_thread():
    global a_star, walls, goal, start, map_creation
    while not map_creation.ready:
        time.sleep(1)

    start = map_creation.start
    goal = map_creation.goal
    walls = map_creation.walls

    a_star = AStar(start, goal, R_C, R_C, walls)

    t2 = threading.Thread(target=star_thread)
    t2.daemon = True
    t2.start() 
    draw_path()   

def draw_path():
    global board, a_star, cost, walls
    #board.draw()
    while cost == None:
        board.draw_coordinates([a_tuple[1] for a_tuple in a_star.openlist.queue], "green")
        board.draw_coordinates(a_star.closedlist, "yellow")
        board.draw_coordinates(a_star.path, "orange")
        
        board.draw_coordinates(walls, "black")
        board.draw_coordinates([start, goal], "blue")

        board.platform.update()
        time.sleep(0.01)

    board.draw()
    board.draw_coordinates(a_star.closedlist, "yellow")
    board.draw_coordinates(walls, "black")
    if cost == -1:
        board.draw_coordinates(a_star.path, "red")
        board.draw_coordinates([start, goal], "blue")
    else:
        board.draw_coordinates(a_star.path, "blue")

    board.platform.update()
    time.sleep(0.01)


board = Board("A*-Algorithm", R_C, R_C, W_H)
map_creation = MapCreation(R_C, W_H, board)
board.draw()

t = threading.Thread(target=creation_thread)
t.daemon = True
t.start()
board.start()


