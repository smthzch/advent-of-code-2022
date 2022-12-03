class ElfSack:
    # construct priority scores
    lower = dict(zip(
        [chr(i) for i in range(97, 123)], # construct lowercase letters, ascii 97-122
        range(1, 27)
    ))
    upper = dict(zip(
        [chr(i) for i in range(65, 91)], # construct uppercase letters, ascii 65-90
        range(27, 53)
    ))
    priority = {**lower, **upper}

    def __init__(self, pth):
        # constructor is called when a new class instance is initialized
        # self is first argument of every class method, it is how all attributes and methods
        # of a class are accessed within a method
        
        with open(pth) as rdr:
            self.lines = rdr.readlines()
    
    def get_duplicate_priorities(self):
        total_priority = 0
        for line in self.lines:
            mid_ix = int(len(line) / 2)
            # RH side is implicitly a tuple, LHS unpacks tuple into separate variables
            bin1, bin2 = set(line[:mid_ix]), set(line[mid_ix:])
            
            intersection = bin1.intersection(bin2)
            for item in intersection:
                total_priority += self.priority[item]
        
        print(f'Total priority: {total_priority}')

    def get_badge_priorities(self):
        total_priority = 0
        for i in range(0, len(self.lines), 3):
            total_priority += self.group_priority(self.lines[i: (i + 3)])

        print(f"Badge priority {total_priority}")

    def group_priority(self, lines):
        n_elfs = len(lines)
        potential_badge = set(self.priority.keys()) # any letter is potential badge

        # loop through unique combinations of elves
        # check which items are shared
        for i in range(n_elfs - 1):
            elf1 = set(lines[i])
            for j in range(i, n_elfs):
                elf2 = set(lines[j])
                shared_items = elf1.intersection(elf2)
                potential_badge = potential_badge.intersection(shared_items)

        assert len(potential_badge) == 1
        badge = list(potential_badge)[0]
        return self.priority[badge]
