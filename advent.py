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

print("---Day 1---")

pth = "data/day{}.txt"
elf_cals = day1.get_elf_cals(pth.format(1))
elf_cals.sort()
print(f"Max cals :{ elf_cals[-1] }")
print(f"Top 3 cals :{ sum(elf_cals[-3:]) }")

print("---Day 2---")
rps_score = day2.get_score1(pth.format(2))
print(f"Total score :{ rps_score }")
rps_score = day2.get_score2(pth.format(2))
print(f"Total score :{ rps_score }")

print("---Day 3---")
sack = day3.ElfSack(pth.format(3))
sack.get_duplicate_priorities()
sack.get_badge_priorities()

print("---Day 4---")
groups = day4.ElfGroup(pth.format(4))
groups.count_contained()
groups.count_overlaps()

print("---Day 5---")
crates = day5.Crates(9, "data/day5_stack.txt")
crates.move_one("data/day5_moves.txt")
crates.move_all("data/day5_moves.txt")

print("---Day 6---")
signal = day6.ElfSignal(pth.format(6))
signal.find_start()

print("---Day 7---")
fs = day7.FileSystem(pth.format(7))
fs.sum_dirs()
fs.to_delete()
