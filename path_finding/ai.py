from queue import Queue, PriorityQueue
import time

def write_marked_map_to_file(marked_map, file_path):
    with open(file_path, 'w') as file:
        for row in marked_map:
            line = ''.join(row)
            file.write(line + '\n')

def h(pos, goal):
    x1, y1 = pos
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

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

def bfs(map_data, start):
    # start can be a tuple (x, y)
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    
    # cost and iteration counter
    cost = 0
    iterations = 0

    while not frontier.empty():
        current = frontier.get()
        iterations += 1
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
        cost += 1
                    
    return path, cost, iterations # return the path from goal to start

def greedy(map_data, start, goal):
    # start can be a tuple (x, y)

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None

    cost = 0
    iterations = 0
    
    while not frontier.empty():
        _, current = frontier.get()
        iterations += 1
        
        # we don't care about all paths, so we should check if current is a diamond.
        if (map_data[current[0]][current[1]] == 'D'): 
            break

        # If it is, we store the coordinates of the diamond and stop the search
        # (implement this yourself)
        
        for next in neighbors(map_data, current):
            if next not in came_from:
                priority = h(next, goal)
                frontier.put((priority, next))
                came_from[next] = current
                
    # Once we found the diamond, reconstruct the path
    # Find an appropriate data structure to represent the path, a list is a natural choice
    #return path
        
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
        cost += 1
                    
    return path, cost, iterations # return the path from goal to start

def astar(map_data, start, goal):
    # start can be a tuple (x, y)

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None
    
    cost_so_far = {}
    cost_so_far[start] = 0
    
    cost = 0
    iterations = 0

    while not frontier.empty():
        _, current = frontier.get()
        iterations += 1
        # we don't care about all paths, so we should check if current is a diamond.

        if (map_data[current[0]][current[1]] == 'D'): 
            break

        # If it is, we store the coordinates of the diamond and stop the search
        # (implement this yourself)
        
        for next in neighbors(map_data, current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + h(next, goal)    # g(n) + h(n)
                frontier.put((priority, next))
                came_from[next] = current
                
    # Once we found the diamond, reconstruct the path
    # Find an appropriate data structure to represent the path, a list is a natural choice
    #return path
        
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
        cost += 1
                    
    return path, cost, iterations # return the path from goal to start


def format_and_print_table(headers, data):
    def print_section(section_data):
        print(header_line)
        print("| " + " | ".join(str(header).ljust(width) for header, width in zip(headers, column_widths)) + " |")
        print(header_line)
        for row in section_data:
            print("| " + " | ".join(str(item).ljust(width) for item, width in zip(row, column_widths)) + " |")
        print(header_line)
        print()

    column_widths = [max(len(str(item)) for item in column) for column in zip(headers, *data)]
    header_line = "+".join("-" * (width + 2) for width in column_widths)

    organized_data = {'BFS': [], 'greedy': [], 'A*': []}

    for row in data:
        algorithm = row[0]
        organized_data[algorithm].append(row)

    for algorithm in ['BFS', 'greedy', 'A*']:
        print_section(organized_data[algorithm])


if __name__ == "__main__":
    
    headers = ('Algorithm', 'Map', 'Cost', 'Iterations', 'Time (s)')
    algorithms = ("BFS", "greedy", "A*")
    
    map_list = (["cave300x300", (2, 2), (295, 257)],
                ["cave600x600", (2, 2), (598, 595)],
                ["cave900x900", (2, 2), (898, 895)])
    
    data = []
    
    for map, start, goal in map_list:
        # Test all maps in map_list with all algorithms
        with open(map) as f:
            map_data = [l.strip() for l in f.readlines() if len(l)>1]
        
        for algo in algorithms:
            if (algo == "BFS"):
                start_time = time.time()
                path, cost, iterations = bfs(map_data, start)
                
            elif (algo == "greedy"):
                start_time = time.time()
                path, cost, iterations = greedy(map_data, start, goal)
                
            else:
                start_time = time.time()
                path, cost, iterations = astar(map_data, start, goal)
                
                
            # Save data
            time_elapsed = time.time() - start_time
            data.append([algo, map, cost, iterations, f"{time_elapsed:.5f}"])
            
            # Write path to file
            marked_map = map_path(map_data, path)
            write_marked_map_to_file(marked_map, f"./results/{map}_{algo}")
        
    
    # Display results
    format_and_print_table(headers, data)