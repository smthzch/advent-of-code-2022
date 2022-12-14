class SandTrap:
    dynamics = [
        (0, 1),
        (-1, 1),
        (1, 1),
        (0, 0)
    ]
    source = (500, 0)

    def __init__(self, pth):
        # read in paths
        paths = []
        with open(pth) as rdr:
            for line in rdr:
                paths += [[
                    list(map(int, node.split(",")))
                    for i, node in enumerate(line.strip().split(" "))
                    if i % 2 == 0
                ]]

        # build set of locations with rock
        self.rock = []
        self.lowest_rock = float("-inf")
        for path in paths:
            start_x, start_y = path[0]
            for node in path[1:]:
                to_x, to_y = node
                x1, x2 = min(start_x, to_x), max(start_x, to_x)
                y1, y2 = min(start_y, to_y), max(start_y, to_y)
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        self.rock += [(x, y)]
                        self.lowest_rock = max(self.lowest_rock, y)
                start_x, start_y = to_x, to_y

        self.rock = set(self.rock)
        self.bottom = self.lowest_rock + 2
        
    def solve(self, criteria):
        assert criteria in ["bottom", "top"]
        if criteria == "bottom":
            self.criteria = lambda sand: sand[1] > self.lowest_rock
        else:
            self.criteria = lambda sand: sand == self.source

        self.filled = set(self.rock) # set of sand and rock
        total_sand = -1
        complete = False
        # dump sand in one grain at a time
        while not complete:
            sand = self.source
            new_sand, complete = self.step(sand)
            # while sand still moving try to keep moving
            while new_sand != sand:
                sand = new_sand
                new_sand, complete = self.step(sand)
                if complete: break
            self.filled.add(sand) # sand stopped so add to filled locations
            total_sand += 1

        total_sand += 1 if criteria == "top" else 0
        print(f"Total sand: {total_sand}")

    def step(self, sand):
        # loop through movement precedence and see if can complete
        for dynamic in self.dynamics:
            new_sand = (sand[0] + dynamic[0], sand[1] + dynamic[1]) # tuple(map(sum, zip(sand, dynamic)))
            complete = self.criteria(new_sand)
            if new_sand not in self.filled and new_sand[1] != self.bottom:
                return new_sand, complete
        raise RuntimeError("All dynamic possibilities exhausted.")
