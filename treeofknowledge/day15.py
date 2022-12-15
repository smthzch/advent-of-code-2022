import re

class Sensor:
    def __init__(self, pth):
        p = re.compile("=-?[0-9]*")
        with open(pth) as rdr:
            pairs = [
                [int(x[1:]) for x in p.findall(line.strip())]
                for line in rdr
            ]

        # get manhattan distances of sensor/beacon pairs
        self.pairs = [
            {
                "sensor": (x[0], x[1]),
                "beacon": (x[2], x[3]),
                "distance": self.manhattan_dist(x)
            }
            for x in pairs
        ]

    def manhattan_dist(self, pair):
        return sum([
            abs(pair[0] - pair[2]),
            abs(pair[1] - pair[3])
        ])

    
    def solve(self, row=2000000):
        beacons = set()
        filled = set()
        
        for pair in self.pairs:
            sensor = pair["sensor"]
            beacon = pair["beacon"]
            distance = pair["distance"]
            row_dist = abs(sensor[1] - row)
            dist_diff = distance - row_dist

            if dist_diff >= 0:
                for d in range(dist_diff + 1):
                    fill_r = (sensor[0] + d, row)
                    fill_l = (sensor[0] - d, row)

                    if fill_r not in beacons:
                        filled.add(fill_r)
                    if fill_l not in beacons:
                        filled.add(fill_l)

            if beacon[1] == row:
                if beacon in filled:
                    filled.remove(beacon)
                beacons.add(beacon)

        print(len(filled))

        #self.print_map(filled)

    def print_map(self, filled, maxv=20):
        m = [
            ["." for x in range(maxv)]
            for y in range(maxv)
        ]

        for fill in filled:
            if fill[0] >= 0 and fill[0] < maxv:
                m[fill[1]][fill[0]] = "#"

        for pair in self.pairs:
            sensor = pair["sensor"]
            beacon = pair["beacon"]

            m[sensor[1]][sensor[0]] = "S"
            m[beacon[1]][beacon[0]] = "B"

        for row in m:
            print("".join(row))

