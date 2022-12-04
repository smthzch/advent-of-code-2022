class ElfGroup:
    def __init__(self, pth):
        self.groups = []            
        with open(pth) as rdr:
            for line in rdr.readlines():
                elf1, elf2 = line.split(",")
                elf1, elf2 = map(self.get_areas, [elf1, elf2])
                self.groups += [
                    [elf1, elf2]
                ]

    def get_areas(self, string):
        start, end = map(int, string.split("-"))
        return [x for x in range(start, end + 1)]

    def count_contained(self):
        count = 0
        for group in self.groups:
            elf1, elf2 = map(set, group)
            count += 1 if elf1.issubset(elf2) or elf2.issubset(elf1) else 0
        print(f"N contained groups {count}")

    def count_overlaps(self):
        count = 0
        for group in self.groups:
            elf1, elf2 = map(set, group)
            count += 1 if not elf1.isdisjoint(elf2) else 0
        print(f"N overlaps {count}")
