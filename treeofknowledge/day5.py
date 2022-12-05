import copy

class Crates:
    def __init__(self, num_stacks, stack_pth):
        self.stacks = [[] for i in range(num_stacks)]
        with open(stack_pth) as f:
            for line in f.readlines():
                row = line.strip().split("]")
                i = 0
                for stack in row:
                    if len(stack) > 1:
                        n_spaces = int(len(stack[:-2]) / 4)
                        i += n_spaces
                        crate = stack[-1]
                        self.stacks[i] += [crate]
                        i += 1

    def move_one(self, moves_pth):
        stacks = copy.deepcopy(self.stacks)
        with open(moves_pth) as f:
            for line in f.readlines():
                cmds = line.strip().split(' ')
                move = int(cmds[1])
                off = int(cmds[3]) - 1
                onto = int(cmds[5]) - 1
                
                for m in range(move):
                    stacks[onto].insert(0, stacks[off][0])
                    stacks[off].pop(0)
        
        print("Top stacks move one: ", end='')
        for stack in stacks:
            print(stack[0], end='')
        print()

    def move_all(self, moves_pth):
        stacks = copy.deepcopy(self.stacks)
        with open(moves_pth) as f:
            for line in f.readlines():
                cmds = line.strip().split(' ')
                move = int(cmds[1])
                off = int(cmds[3]) - 1
                onto = int(cmds[5]) - 1

                stacks[onto] = stacks[off][0:move] + stacks[onto]
                stacks[off] = stacks[off][move:]
        
        print("Top stacks move all: ", end='')
        for stack in stacks:
            print(stack[0], end='')
        print()
