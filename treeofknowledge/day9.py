import numpy as np

class Rope:
    move_map = {
        "U": np.array([0, 1]),
        "R": np.array([1, 0]),
        "D": np.array([0, -1]),
        "L": np.array([-1, 0])
    }

    def __init__(self, pth):
        with open(pth) as rdr:
            self.moves = [
                line.strip().split(" ")
                for line in rdr.readlines()
            ]

    def find_visited(self, n_knots):
        self.reset(n_knots)

        for move in self.moves:
            direction = move[0]
            distance = int(move[1])

            # move knots one space at a time
            for i in range(distance):
                self.knots[0] += self.move_map[direction] # move the head
                for k in range(self.n_knots - 1):
                    # move each knot in turn if needed
                    diff = self.knots[k] - self.knots[k + 1]
                    self.knots[k + 1] += self.move_tail(diff)

                # track the tail
                tail = self.knots[-1].tolist()
                if tail not in self.visited:
                    self.visited += [tail]

        print(f"Locations visited by tail {len(self.visited)}")

    def move_tail(self, diff):
        gt = np.abs(diff) > 1
        if not gt.any(): # if not more than one space away dont move
            return np.array([0, 0])
        else:
            # scale to unit distance (per dim) to get move
            sign = np.sign(diff)
            diff[gt] = sign[gt]
            return diff

    def reset(self, n_knots):
        self.n_knots = n_knots
        self.knots = [np.array([0, 0]) for k in range(n_knots)]
        self.visited = [[0, 0]]
