from math import floor

class CRT:
    def __init__(self, pth, offset=20, modulo=40, width=40, height=6):
        with open(pth) as rdr:
            self.cmds = [
                line.strip().split(" ")
                for line in rdr.readlines()
            ]

        self.offset = offset
        self.modulo = modulo
        self.width = width
        self.height = height

    def run_program(self):
        self.screen = self.create_screen()
        strengths = []
        self.cycle = 0
        self.x = 1
        for cmd in self.cmds:
            if cmd[0] == "addx":
                y = int(cmd[1])

                self.step()
                strengths += self.check_x()
                self.step()
                strengths += self.check_x()

                self.x += y
            else:
                self.step()
                strengths += self.check_x()

        print(f"Sum of strengths {sum(strengths)}")
        self.print_screen()

    def check_x(self):
        if (self.cycle + self.offset) % self.modulo == 0:
            return [self.x * self.cycle]
        return []

    def create_screen(self):
        return [
            ["." for j in range(self.width)]
            for i in range(self.height)
        ]

    def print_screen(self):
        print("\n".join(
            [
                "".join(row)
                for row in self.screen
            ]
        ))

    def step(self):
        i = floor(self.cycle / self.width)
        j = self.cycle % self.width
        self.cycle += 1

        if j in [self.x + z for z in [-1, 0, 1]]:
            self.screen[i][j] = "#"
        