from queue import Queue

def map_path(map, path):
    # convert the map to a list of lists to make it mutable
    mapped_path = [list(row) for row in map]
    col_dim = len(map[0])
    row_dim = len(map)
    
    for x, y in path:
        if 0 <= x < row_dim and 0 <= y < col_dim:
            if (mapped_path[x][y] != 'D' and mapped_path[x][y] != 's'):
                mapped_path[x][y] = '.'

    return mapped_path

def neighbors(map, current):
    x, y = current
    moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] # move list for bfs
    valid_neighbors = []

    for move_x, move_y in moves:
        # check if out of bounds
        try:
            if (map[move_x][move_y] != '*'):
                valid_neighbors.append((move_x,move_y))
        except:
            pass

    return valid_neighbors

def my_search(map_data, start):
    # start can be a tuple (x, y)

    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        # we don't care about all paths, so we should check if current is a diamond.
        if (map_data[current[0]][current[1]] == 'D'): 
            break
        
        # If it is, we store the coordinates of the diamond and stop the search
        # (implement this yourself)
        
        for next in neighbors(map_data, current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
            
    # Once we found the diamond, reconstruct the path
    # Find an appropriate data structure to represent the path, a list is a natural choice
    #return path
        
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
                    
    return path # return the path from goal to start


lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]
start_row=14
start_col=16
start = (start_row, start_col)
    
path = my_search(lava_map1, start)

marked_map = map_path(lava_map1, path)

for row in marked_map:
    print(''.join(row))
