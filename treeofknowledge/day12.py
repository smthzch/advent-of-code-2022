class Elevation:
    neighbors = [
        [-1, 0],
        [0, -1],
        [1, 0],
        [0, 1]
    ]

    def __init__(self, pth):
        self.map = []
        self.start = [-1, -1, -1]
        self.end = [-1, -1, -1]
        
        with open(pth) as rdr:
            for i, line in enumerate(rdr):
                row = []
                for j, spot in enumerate(line.strip()):
                    if spot == "S":
                        height = ord("a")
                        self.start = [i, j, height]
                    elif spot == "E":
                        height = ord("z")
                        self.end = [i, j, height]
                    else:
                        height = ord(spot)
                    row += [height]
                self.map += [row]

        self.height = len(self.map)
        self.width = len(self.map[0])

    def hill_climb(self):
        paths = [[self.start]]
        self.visited = [self.start]
        
        # find shortest path from provided start
        while len(paths) > 0:
            current_path = paths.pop(0)
            if current_path[-1] == self.end:
                break
            paths += self.get_neighbors(current_path)
        
        print(f"Steps taken: {len(current_path) - 1}")

        # find latest low point in found path
        shortest_path = float("inf")
        for i in range(len(current_path)):
            if current_path[i][2] == ord("a"):
                shortest_path = len(current_path[i:]) - 1

        # find all non-visited low spots
        for i, row in enumerate(self.map):
            for j, height in enumerate(row):
                if height == ord("a"):
                    node = [i, j, height]
                    if node not in self.visited:
                        paths += [[node]]
                        self.visited += [node]

        # find shortest path from new starts
        while len(paths) > 0:
            current_path = paths.pop(0)
            if current_path[-1] == self.end:
                path_length = len(current_path) - 1
                shortest_path = min(path_length, shortest_path)
                continue
            paths += self.get_neighbors(current_path)
        
        print(f"Steps taken: {shortest_path}")

    def get_neighbors(self, path):
        current_node = path[-1]
        new_paths = []
        for neighbor in self.neighbors:
            # find new location and height
            new_loc = [current_node[0] + neighbor[0], current_node[1] + neighbor[1]]
            try: # looking up height in map can fail if out of bounds
                new_height = self.map[new_loc[0]][new_loc[1]]
                new_node = new_loc + [new_height]
                if self.valid_move(new_node, current_node[2]):
                    # extend path
                    new_paths += [path + [new_node]]
                    self.visited += [new_node]
            except:
                pass
        return new_paths

    def valid_move(self, loc, current_height):
        valid = True if loc not in self.visited else False
        valid = valid if current_height + 1 >= loc[2] else False
        valid = valid if loc[0] >= 0 and loc[0] < self.height else False
        valid = valid if loc[1] >= 0 and loc[1] < self.width else False
        return valid

    def print_map(self):
        for i, row in enumerate(self.map):
            print(i, " ", end="")
            for spot in row:
                print(chr(spot), end="")
            print("")

    def print_path(self, path):
        for node in path:
            self.map[node[0]][node[1]] = 43
        self.print_map()
