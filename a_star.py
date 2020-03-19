class PriorityQueue():
    '''Implements simple PriorityQueue'''

    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0

    # adds coordinate or updates priority
    def insert(self, coordinate, priority):
        for i in range(len(self.queue)):
            p, c = self.queue[i]
            if c == coordinate:
                del self.queue[i]
        self.queue.append((priority, coordinate))
    
    def get_priority(self, coordinate):
        for i in range(len(self.queue)):
            p, c = self.queue[i]
            if c == coordinate:
                return p
        return None
    
    def get_max(self):
        max = 0
        for i in range(len(self.queue)):
            p, c = self.queue[i]
            pm, cm = self.queue[max]
            if p > pm:
                max = i
        data = self.queue[max]
        del self.queue[max]
        return data
    
    def get_min(self):
        min = 0
        for i in range(len(self.queue)):
            p, c = self.queue[i]
            pm, cm = self.queue[min]
            if p < pm:
                min = i
        data = self.queue[min]
        del self.queue[min]
        return data


class Neighbours:
    '''Get neighbouring tiles'''

    def __init__(self, width, height, walls):
        self.width = width
        self.height = height
        self.walls = walls

    def on_board(self, coordinate):
        # Square on board grid
        (x, y) = coordinate
        return 0 <= x < self.width and 0 <= y < self.height
    
    def no_wall(self, coordinate):
        return coordinate not in self.walls

    def get_neighbours(self, coordinate):
        (x, y) = coordinate
        result = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        result = filter(self.on_board, result)
        result = filter(self.no_wall, result)
        return result
    
    def cost(self, from_node, to_node):
        return 1


class AStar:
    '''A*-Algorithm'''

    def __init__(self, start, goal, width, height, walls):
        self.openlist = PriorityQueue()
        self.openlist.insert(start, 0)
        self.closedlist = []
        self.precessor = {}
        self.start = start
        self.goal = goal
        self.neighbours = Neighbours(width, height, walls)
    
    def heuristic(self, coordinate):
        cx, cy = coordinate
        gx, gy = self.goal
        dx = abs(cx - gx)
        dy = abs(cy - gy)
        return dx+dy

    def neighbours_to_open_list(self, curr):
        p, c = curr
        neighbours = self.neighbours.get_neighbours(c)
        for neighbour in neighbours:
            if not neighbour in self.closedlist: # if neighbour wasn't visited before
                p, c = curr
                n_cost_g = p + self.neighbours.cost(c, neighbour)
                n_priority = self.openlist.get_priority(c) # if coordinate already in list + the priority else None
                if not n_priority == None and n_priority > n_cost_g:
                    n_cost_f = n_cost_g + self.heuristic(neighbour)
                    self.openlist.insert(neighbour, n_cost_f)
                    self.precessor[neighbour] = curr

    def search(self):
        while not self.openlist.is_empty():
            curr = self.openlist.get_min()
            p, c = curr
            print(self.closedlist)
            if c == self.goal:
                return p
            self.closedlist.append(c)

            self.neighbours_to_open_list(curr)
            
        #couldn't find path
        return None
    
    def get_path(self):
        curr = self.goal
        path = []
        while curr != self.start:
            path.append(curr)
            curr = self.precessor[curr]
        path.append(self.start)
        path.reverse()
        return path