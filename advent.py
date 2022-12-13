from treeofknowledge import *

welcome = """######################################
#
#
# ADVENT OF CODE 2022
#
#
######################################
"""
print(welcome)

printd = lambda x: print(f"---Day {x}---")

printd(1)
pth = "data/day{}.txt"
elf_cals = day1.get_elf_cals(pth.format(1))
elf_cals.sort()
print(f"Max cals :{ elf_cals[-1] }")
print(f"Top 3 cals :{ sum(elf_cals[-3:]) }")

printd(2)
rps_score = day2.get_score1(pth.format(2))
print(f"Total score :{ rps_score }")
rps_score = day2.get_score2(pth.format(2))
print(f"Total score :{ rps_score }")

printd(3)
sack = day3.ElfSack(pth.format(3))
sack.get_duplicate_priorities()
sack.get_badge_priorities()

printd(4)
groups = day4.ElfGroup(pth.format(4))
groups.count_contained()
groups.count_overlaps()

printd(5)
crates = day5.Crates(9, "data/day5_stack.txt")
crates.move_one("data/day5_moves.txt")
crates.move_all("data/day5_moves.txt")

printd(6)
signal = day6.ElfSignal(pth.format(6))
signal.find_start()

printd(7)
fs = day7.FileSystem(pth.format(7))
fs.sum_dirs()
fs.to_delete()

printd(8)
treehouse = day8.TreeHouse(pth.format(8))
treehouse.count_visible()
treehouse.max_scenic_score()

printd(9)
rope = day9.Rope(pth.format(9))
#rope.find_visited(n_knots=2)
#rope.find_visited(n_knots=10)

printd(10)
crt = day10.CRT(pth.format(10))
crt.run_program()

printd(11)
monkeys = day11.Monkeys(pth.format(11))
monkeys.monkey_business(rounds=20, relief=True)
monkeys = day11.Monkeys(pth.format(11))
monkeys.monkey_business(rounds=10_000, relief=False)

printd(12)
topo = day12.Elevation(pth.format(12))
topo.hill_climb()

printd(13)
decoder = day13.Decoder(pth.format(13))
decoder.correct()
decoder.bubble_sort()
